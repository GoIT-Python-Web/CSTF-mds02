import asyncio
import json


async def ping_connect(writer):
    writer.write(b'\x01')
    await writer.drain()


async def receive_data(reader, chunk_size=100):
    data = await reader.read(chunk_size)
    print(f"Received {data}")
    return data


async def main(numbers):
    result = None
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    await ping_connect(writer)
    response = await receive_data(reader)
    if response == b'Allowed':
        writer.write(json.dumps(numbers).encode())
        await writer.drain()
        result = await receive_data(reader, 10 * 1024)
    else:
        print("Denied")
    writer.close()
    await writer.wait_closed()
    return result


if __name__ == '__main__':
    r = asyncio.run(main([24, 34, 22]))
    print(r.decode())
