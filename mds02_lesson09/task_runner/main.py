import asyncio
import logging

from aiopath import AsyncPath
from aiofile import async_open

message_format = "%(processName)s %(asctime)s: %(message)s"
logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")


async def consumer(queue: asyncio.Queue):
    async with async_open("main.js", "w", encoding="utf-8") as f:
        while True:
            file, blob = await queue.get()
            logging.info(f"Write file {file.name}")
            await f.write(f"{blob}\n")
            queue.task_done()


async def producer(file: AsyncPath, q: asyncio.Queue):
    async with async_open(file, "r", encoding="utf-8") as f:
        data = []
        async for line in f:
            data.append(str(line))
        await q.put((file, "".join(data)))


async def main():
    files_for_reading = asyncio.Queue()

    list_files = AsyncPath(".").joinpath("files").glob("*.js")
    print(list_files)
    producers = [
        asyncio.create_task(producer(file, files_for_reading))
        async for file in list_files
    ]
    consumer_task = asyncio.create_task(consumer(files_for_reading))

    await asyncio.gather(*producers)
    await files_for_reading.join()
    consumer_task.cancel()


if __name__ == "__main__":
    asyncio.run(main())
