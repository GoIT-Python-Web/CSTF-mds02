from functools import wraps
from time import time


def async_timed(*, name: str = None, format=4):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start = time()
            result = await func(*args, **kwargs)
            end = time()
            if name:
                print(f"{name} finished in {end - start:.{format}f} sec")
            else:
                print(f"finished in {end - start:.4f} sec")
            return result

        return wrapper

    return decorator
