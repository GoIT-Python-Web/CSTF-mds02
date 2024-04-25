import string
import asyncio

from collections import defaultdict

import httpx


async def get_text(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None


# Функція для видалення знаків пунктуації
def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))


async def map_function(word) -> tuple:
    return word, 1


def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()


async def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)


# Виконання MapReduce
async def map_reduce(text, search_words=None):
    text = await get_text(url)
    if text:
        # Видалення знаків пунктуації
        text = remove_punctuation(text)
        words = text.split()

        # Якщо задано список слів для пошуку, враховувати тільки ці слова
        if search_words:
            words = [word for word in words if word in search_words]  # filter

        # Паралельний Мапінг
        mapped_values = await asyncio.gather(*[map_function(word) for word in words])

        # Крок 2: Shuffle
        shuffled_values = shuffle_function(mapped_values)

        # Паралельна Редукція
        reduced_values = await asyncio.gather(*[reduce_function(key_values) for key_values in shuffled_values])

        return dict(reduced_values)
    else:
        return None


if __name__ == '__main__':
    # Вхідний текст для обробки
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    # Виконання MapReduce на вхідному тексті
    search_words = ['brother', 'Brother', 'Big', 'big', 'hate', "Hate", 'peace']
    result = asyncio.run(map_reduce(url, search_words))

    print("Результат підрахунку слів:", result)
