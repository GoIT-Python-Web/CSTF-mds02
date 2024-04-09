import logging

import psycopg2
from contextlib import contextmanager
from dotenv import dotenv_values

config = dotenv_values('.env')


@contextmanager
def connect():
    try:
        conn = psycopg2.connect(host=config['PG_HOST'], database=config['PG_DB'], user=config['PG_USER'],
                                password=config['PG_PASSWORD'])
        try:
            yield conn
        finally:
            conn.close()
    except psycopg2.OperationalError as e:
        logging.error(e)
