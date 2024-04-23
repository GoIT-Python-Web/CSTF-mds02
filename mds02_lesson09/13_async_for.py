import asyncio
from time import sleep, time
from typing import AsyncGenerator, Any, AsyncIterator

from faker import Faker

from timing import async_timed

fake = Faker("uk-UA")
fake.seed_instance(42)


async def get_user_form_db(uuid: int) -> dict[str, int | Any]:
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.name(), "email": fake.email()}


async def get_users(uuids: list[int]) -> AsyncGenerator[dict, None]:
    for uuid in uuids:
        yield get_user_form_db(uuid)


@async_timed(name="async_for")
async def main(users: AsyncIterator):
    new_users = []
    async for user in users:
        new_users.append(user)
    result = await asyncio.gather(*new_users)
    return result


if __name__ == "__main__":
    u = asyncio.run(main(get_users([1, 2, 3])))
    print(u)
