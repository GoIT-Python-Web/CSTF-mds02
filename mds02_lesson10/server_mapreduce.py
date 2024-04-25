import asyncio
import json
from collections import defaultdict


async def handler(reader, writer):
    # Перевірка можливості підключення
    connect = await reader.read(100)
    if connect == b'\x01':
        writer.write(b'Allowed')
        await writer.drain()
    else:
        writer.write(b'Denied')
        writer.close()
        await writer.wait_closed()
        return
    # Читання даних
    data = await reader.read(100 * 1024)
    text = data.decode()
    address = writer.get_extra_info('peername')
    print(f'Received {data} from {address}')
    # Відправка даних
    try:
        result = await map_reduce(text)
        print(f'Result: {result}')
        writer.write(json.dumps(result).encode())
        await writer.drain()
    except json.JSONDecodeError:
        print(b'Invalid JSON')
        writer.write(json.dumps({"error": 'Invalid JSON'}).encode())
    finally:
        print(f'Closing connection to {address}')
        writer.close()
        await writer.wait_closed()


async def main():
    server = await asyncio.start_server(handler, '127.0.0.1', 8888)
    adrress = server.sockets[0].getsockname()
    print(f'Serving on {adrress}')
    async with server:
        try:
            await server.serve_forever()
        except asyncio.exceptions.CancelledError:
            print("Server stopped!")
        # finally:
        #     server.close()
        #     await server.wait_closed()
        #     print("Server closed!")


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
async def map_reduce(text):
    # Видалення знаків пунктуації
    words = text.split()

    # Паралельний Мапінг
    mapped_values = await asyncio.gather(*[map_function(word) for word in words])

    # Крок 2: Shuffle
    shuffled_values = shuffle_function(mapped_values)

    # Паралельна Редукція
    reduced_values = await asyncio.gather(*[reduce_function(key_values) for key_values in shuffled_values])

    return dict(reduced_values)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')
