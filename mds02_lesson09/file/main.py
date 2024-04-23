"""
Відсортувати файли в папці.
"""

import argparse
import asyncio
from typing import Coroutine, Any

from aiopath import AsyncPath
from aioshutil import copyfile
import logging

"""
--source [-s] 
--output [-o] default folder = dist
"""

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = AsyncPath(args.get("source"))
output = AsyncPath(args.get("output"))


async def grabs_folder(path: AsyncPath):
    async for el in path.iterdir():
        if await el.is_dir():
            await grabs_folder(el)
        else:
            await copy_file(el)


async def copy_file(file: AsyncPath):
    ext_folder = output / file.suffix[1:]
    try:
        await ext_folder.mkdir(exist_ok=True, parents=True)
        await copyfile(file, ext_folder / file.name)
    except OSError as err:
        logging.error(err)


if __name__ == "__main__":
    message_format = "%(threadName)s %(asctime)s: %(message)s"
    logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")

    asyncio.run(grabs_folder(source))
    print(f"Можна видалять {source}")
