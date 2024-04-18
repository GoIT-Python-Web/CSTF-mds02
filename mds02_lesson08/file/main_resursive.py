"""
Відсортувати файли в папці.
"""

import argparse
import logging
from pathlib import Path
from shutil import copyfile
from multiprocessing import Process, current_process
from sys import exit

"""
--source [-s] 
--output [-o] default folder = dist
"""

message_format = "%(processName)s %(asctime)s: %(message)s"
logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = Path(args.get("source"))
output = Path(args.get("output"))


def grabs_folder(path: Path) -> None:
    logging.info(f"Getting folders from {path}: {current_process().name}")
    for el in path.iterdir():
        if el.is_dir():
            inner_process = Process(target=grabs_folder, args=(el,))
            inner_process.start()
        else:
            copy_file(el)


def copy_file(file: Path) -> None:
    ext_folder = output / file.suffix[1:]
    try:
        ext_folder.mkdir(exist_ok=True, parents=True)
        copyfile(file, ext_folder / file.name)
    except OSError as err:
        logging.error(err)
        exit(1)


if __name__ == "__main__":
    process = Process(target=grabs_folder, args=(source,))
    process.start()
    process.join()
    print(f"Можна видалять {source}")
