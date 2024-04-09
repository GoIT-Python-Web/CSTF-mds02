import logging
from psycopg2 import DatabaseError

from connect_pg import connect


def create_table(conn, sql_stmt: str):
    cursor = conn.cursor()
    try:
        cursor.execute(sql_stmt)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        cursor.close()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    stmt = """
    CREATE TABLE IF NOT EXISTS contacts (
      id SERIAL PRIMARY KEY,
      name VARCHAR(130),
      email VARCHAR(130),
      phone VARCHAR(130),
      age smallint CHECK (age > 0 AND age < 120)
    );
    """

    try:
        with connect() as conn:
            create_table(conn, stmt)
    except RuntimeError as e:
        logging.error(e)