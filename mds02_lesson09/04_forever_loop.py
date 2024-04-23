import asyncio
from random import randint


async def ping(signal):
    print(f"ping {signal}")


async def pong(signal):
    await asyncio.sleep(0.7)
    print(f"pong {signal}")


async def main():
    while True:
        signal = randint(1, 100)
        await ping(signal)
        await pong(signal)


if __name__ == "__main__":
    asyncio.run(main())
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.create_task(main())
    # loop.create_task(ping(42))
    # loop.run_forever()

