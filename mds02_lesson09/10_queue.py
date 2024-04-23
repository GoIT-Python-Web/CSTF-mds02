import asyncio
from random import randint


async def producer(q: asyncio.Queue):
    num = randint(0, 1000)
    await asyncio.sleep(0.1)
    await q.put(num)


async def consumer(q: asyncio.Queue):
    while True:
        num = await q.get()
        print(f"Consumed: {num}: {num**2}")
        q.task_done()


async def main():
    q = asyncio.Queue()
    producers = [asyncio.create_task(producer(q)) for _ in range(200)]
    consumers = [asyncio.create_task(consumer(q)) for _ in range(10)]
    await asyncio.gather(*producers)
    await q.join()
    [c.cancel() for c in consumers]


if __name__ == "__main__":
    asyncio.run(main())
