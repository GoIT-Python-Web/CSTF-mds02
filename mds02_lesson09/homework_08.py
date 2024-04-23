import multiprocessing
from collections import defaultdict
from pathlib import Path
import time


def search_in_file(file_path, keywords, results_queue):
    try:
        with open(file_path, "r") as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    results_queue.put((keyword, file_path))
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")


def process_task(files, keywords, results_queue):
    for file in files:
        search_in_file(file, keywords, results_queue)


def main_multiprocessing(file_paths, keywords):
    start_time = time.time()
    num_processes = 4
    files_per_process = len(file_paths) // num_processes
    processes = []
    results_queue = multiprocessing.Queue()
    results = defaultdict(list)

    for i in range(num_processes):
        start = i * files_per_process
        end = None if i == num_processes - 1 else start + files_per_process
        process_files = file_paths[start:end]
        process = multiprocessing.Process(
            target=process_task, args=(process_files, keywords, results_queue)
        )
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    while not results_queue.empty():
        keyword, file_path = results_queue.get()
        results[keyword].append(file_path)

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    return results


if __name__ == "__main__":
    # Приклад виклику
    file_paths = list(Path("./example").glob("*.py"))
    keywords = ["modify_", "multiprocessing"]
    results = main_multiprocessing(file_paths, keywords)
    print(results)
