import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect_pg import connect


fake = Faker('uk_UA')
COUNT = 1_000


def insert_data(conn, sql_stmt: str):
    cursor = conn.cursor()
    try:
        for _ in range(COUNT):
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            age = randint(1, 100)
            cursor.execute(sql_stmt, (name, email, phone, age))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        cursor.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    stmt = """
    INSERT INTO contacts (name, email, phone, age) VALUES (%s, %s, %s, %s);
    """

    try:
        with connect() as conn:
            insert_data(conn, stmt)
    except RuntimeError as e:
        logging.error(e)
