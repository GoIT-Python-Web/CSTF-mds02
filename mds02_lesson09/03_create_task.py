import asyncio
from time import sleep, time

from faker import Faker

fake = Faker('uk-UA')
fake.seed_instance(42)


# Awaitable -> Coroutine
# Awaitable -> Future -> Task

async def get_user_form_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 4):
        task = asyncio.create_task(get_user_form_db(i))
        users.append(task)

    result = await asyncio.gather(*users)
    return result


if __name__ == "__main__":
    start = time()
    u = asyncio.run(main())
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # u = loop.run_until_complete(main())
    print(u)
    print(time() - start)
