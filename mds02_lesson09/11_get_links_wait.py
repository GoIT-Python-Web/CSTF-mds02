import asyncio
from concurrent.futures import ThreadPoolExecutor

import requests
from icecream import ic
from requests.exceptions import InvalidSchema, MissingSchema, SSLError

from timing import async_timed


urls = [
    "http://www.google.com",
    "http://www.python.org",
    "http://duckduckgo.com",
    "http://www.yahoo.com",
    "http://www.bing.com",
]


def preview_fetch(url):
    try:
        r = requests.get(url)
        return url, r.text[:50]
    except (InvalidSchema, MissingSchema, SSLError) as err:
        ic(f"Error: {err} for {url} skipped")


@async_timed(name="requests")
async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [loop.run_in_executor(executor, preview_fetch, url) for url in urls]
        done, pending = await asyncio.wait(futures, return_when=asyncio.ALL_COMPLETED)
        print(f"Done: {done}, Pending: {pending}")
        [task.cancel() for task in pending]
        return done


if __name__ == "__main__":
    results = asyncio.run(preview_fetch_async())
    print(results)
