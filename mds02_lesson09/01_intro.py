import asyncio


async def foo():
    await asyncio.sleep(0)
    return "foo"


async def main():
    result = await foo()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())
