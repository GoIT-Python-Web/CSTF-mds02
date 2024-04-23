import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def read_file(filename):
    with open(filename) as f:
        return f.read(100)


def calculate(power, p):
    r = [i ** power for i in range(10 ** p)]
    return sum(r)


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as executor:
        results = await loop.run_in_executor(executor, read_file, "timing.py")
        print(results)

    with ProcessPoolExecutor() as executor:
        results = await loop.run_in_executor(executor, calculate, 3, 4)
        print(results)


if __name__ == "__main__":
    asyncio.run(main())
