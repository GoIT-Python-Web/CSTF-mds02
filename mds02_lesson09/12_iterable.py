import asyncio
from time import sleep, time
from typing import Coroutine, Any, Iterable, Awaitable

from faker import Faker

from timing import async_timed

fake = Faker("uk-UA")
fake.seed_instance(42)


async def get_user_form_db(uuid: int) -> dict[str, int | Any]:
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.name(), "email": fake.email()}


def get_users(uuids: list[int]) -> Iterable[Awaitable[dict[str, int | Any]]]:
    return [get_user_form_db(uuid) for uuid in uuids]


@async_timed(name="async_for")
async def main(users):
    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":
    u = asyncio.run(main(get_users([1, 2, 3])))
    print(u)
