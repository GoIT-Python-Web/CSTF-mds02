import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from random import randint


async def ping(signal):
    print(f"ping {signal}")


async def worker():
    while True:
        await asyncio.sleep(0.5)
        signal = randint(1, 100)
        await ping(signal)


def calculate(counter: int):  # CPU bound operation
    init = counter
    while counter > 0:
        counter -= 1
    print(f"Completed operation {init}")
    return f"Completed operation {init}"


async def main():
    loop = asyncio.get_running_loop()
    task = loop.create_task(worker())

    with ProcessPoolExecutor() as executor:
        futures = [loop.run_in_executor(executor, calculate, counter) for counter in
                   [100_000_000, 200_000_000, 300_000_000]]
        results = await asyncio.gather(*futures)
        return results


if __name__ == "__main__":
    r = asyncio.run(main())
    print(r)
