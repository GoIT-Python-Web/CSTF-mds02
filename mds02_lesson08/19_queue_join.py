from multiprocessing import JoinableQueue, Process
from time import sleep
import sys


def worker(q: JoinableQueue, name: str):
    print(f"Starting {name}")
    value = q.get()
    try:
        print(f"{name}:  {value ** 2}")
    except TypeError:
        print(f"{name}:  {value}")
        sys.exit(1)
    finally:
        q.task_done()
    sys.exit(0)


if __name__ == "__main__":
    q = JoinableQueue()
    p1 = Process(target=worker, args=(q, "worker1"))
    p2 = Process(target=worker, args=(q, "worker2"))
    p1.start()
    p2.start()

    q.put(10)
    q.put('foo')
    # q.put(100)
    q.join()

    p1.join()
    p2.join()
    print(p1.exitcode)
    print(p2.exitcode)
    print(q.empty())
