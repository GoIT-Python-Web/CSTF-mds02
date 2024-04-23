import asyncio
import platform

import aiohttp
from icecream import ic


class HttpError(Exception): ...


async def request(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise HttpError(f"Request error: {response.status} to {url}")

        except (
            aiohttp.ClientError,
            aiohttp.ClientConnectionError,
            aiohttp.InvalidURL,
        ) as exc:
            raise HttpError(f"Connection error: {exc} to {url}")


async def main():
    try:
        url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
        response = await request(url)
        return response
    except HttpError as exc:
        ic(exc)


if __name__ == "__main__":
    if platform.system() == "Windows":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    result = asyncio.run(main())
    ic(result)
