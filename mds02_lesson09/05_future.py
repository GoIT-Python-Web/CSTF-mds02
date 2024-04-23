import asyncio
from time import sleep, time

from faker import Faker

from timing import async_timed

fake = Faker('uk-UA')
fake.seed_instance(42)


# Awaitable -> Coroutine
# Awaitable -> Future -> Task

async def get_user_form_db(uuid: int, future: asyncio.Future):
    await asyncio.sleep(0.5)
    future.set_result({"id": uuid, "username": fake.name(), "email": fake.email()})


def make_request(uuid: int):
    future = asyncio.Future()
    asyncio.create_task(get_user_form_db(uuid, future))
    return future


@async_timed(name="main", format=3)
async def main():
    """

    :return: Users
    """
    users = []
    for i in range(1, 4):
        users.append(make_request(i))

    print([u.done() for u in users])
    result = await asyncio.gather(*users)
    print([u.done() for u in users])
    return result


if __name__ == "__main__":
    u = asyncio.run(main())
    print(u)
