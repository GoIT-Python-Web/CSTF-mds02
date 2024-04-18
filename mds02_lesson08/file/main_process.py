"""
Відсортувати файли в папці.
"""

import argparse
from pathlib import Path
from shutil import copyfile
from multiprocessing import Pool, cpu_count, current_process
import logging

"""
--source [-s] 
--output [-o] default folder = dist
"""
message_format = "%(processName)s %(asctime)s: %(message)s"
logging.basicConfig(format=message_format, level=logging.INFO, datefmt="%H:%M:%S")

parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = Path(args.get("source"))
output = Path(args.get("output"))


def grabs_folder(path: Path) -> list[Path]:
    folders = []
    for el in path.iterdir():
        if el.is_dir():
            folders.append(el)
            inner_folders = grabs_folder(el)
            if len(inner_folders) > 0:
                folders += inner_folders
    return folders


def copy_file(path: Path) -> None:
    logging.info(f"Getting folders from {path}: {current_process().name}")
    for el in path.iterdir():
        if el.is_file():
            ext_folder = output / el.suffix[1:]
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copyfile(el, ext_folder / el.name)
            except OSError as err:
                logging.error(err)


if __name__ == "__main__":
    folders = [source, *grabs_folder(source)]  # [source] + grabs_folder(source)
    print(folders)

    with Pool(processes=cpu_count()) as pool:
        pool.map(copy_file, folders)

    print(f"Можна видалять {source}")
