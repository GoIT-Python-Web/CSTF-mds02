import asyncio
from time import sleep, time

from faker import Faker

fake = Faker('uk-UA')
fake.seed_instance(42)


def get_user_form_db(uuid: int):
    sleep(0.5)
    return {"id": uuid, "username": fake.name(), "email": fake.email()}


async def get_async_user_form_db(uuid: int):
    await asyncio.sleep(0.5)
    return {"id": uuid, "username": fake.name(), "email": fake.email()}


async def main():
    users = []
    for i in range(1, 4):
        users.append(get_async_user_form_db(i))

    result = await asyncio.gather(*users)
    return result

if __name__ == "__main__":
    start = time()
    for i in range(1, 4):
        u = get_user_form_db(i)
        print(u)
    print(time() - start)

    start = time()
    u = asyncio.run(main())
    print(u)
    print(time() - start)
