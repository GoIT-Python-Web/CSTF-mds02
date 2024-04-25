import asyncio
import json


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
    data = await reader.read(10*1024)
    data = data.decode()
    address = writer.get_extra_info('peername')
    print(f'Received {data} from {address}')
    # Відправка даних
    try:
        numbers = json.loads(data)
        squares = await compute_squares(numbers)
        print(f'Result: {squares}')
        writer.write(json.dumps(squares).encode())
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


async def compute_squares(numbers):
    return [number * number for number in numbers]

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye!')
