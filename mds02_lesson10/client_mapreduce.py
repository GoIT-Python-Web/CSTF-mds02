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


async def ping_connect(writer):
    writer.write(b'\x01')
    await writer.drain()


async def receive_data(reader, chunk_size=100):
    data = await reader.read(chunk_size)
    print(f"Received {data}")
    return data


async def main(url):
    result = None
    text = await get_text(url)
    if text:
        # Видалення знаків пунктуації
        text = remove_punctuation(text)
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        await ping_connect(writer)
        response = await receive_data(reader)
        if response == b'Allowed':
            writer.write(text.encode())
            await writer.drain()
            result = await receive_data(reader, 100 * 1024)
        else:
            print("Denied")
        writer.close()
        await writer.wait_closed()
    return result


if __name__ == '__main__':
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    r = asyncio.run(main(url))
    print(r.decode())
