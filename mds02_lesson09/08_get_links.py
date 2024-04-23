import asyncio
import requests
from concurrent.futures import ThreadPoolExecutor

from timing import async_timed


urls = [
    "http://www.google.com",
    "http://www.python.org",
    "http://duckduckgo.com",
    "http://www.yahoo.com",
    "http://www.bing.com",
    "htttp://www.baidu.com",
]


def preview_fetch(url):
    r = requests.get(url)
    return url, r.text[:50]


@async_timed(name="requests")
async def preview_fetch_async():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [loop.run_in_executor(executor, preview_fetch, url) for url in urls]
        result = await asyncio.gather(*futures, return_exceptions=True)
        return result


if __name__ == "__main__":
    res = asyncio.run(preview_fetch_async())
    results = [r for r in res if not isinstance(r, Exception)]
    print(results)
