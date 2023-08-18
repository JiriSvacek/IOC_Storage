from psycopg2.extras import execute_values
from psycopg2 import errors
import psycopg2


def exception_handler(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except errors.UndefinedTable as e:
            print("Table does not exist:", e)
            return [(None,)]

    return wrapper


class MyDB:
    URLS = "urls"
    IP_ADDRESSES = "ip_addresses"

    def __init__(self, connect: psycopg2.connect):
        self.connection = connect
        self.connection.autocommit = True
        self.curs = self.connection.cursor()
        self.create_tables()

    def create_tables(self) -> None:
        """Creates two table with id as primary key, address and origin."""
        self.curs.execute(f"""CREATE TABLE IF NOT EXISTS {self.IP_ADDRESSES} (id SERIAL PRIMARY KEY,
                            address TEXT UNIQUE, origin TEXT)""")
        self.curs.execute(f"""CREATE TABLE IF NOT EXISTS {self.URLS} (id SERIAL PRIMARY KEY, address TEXT UNIQUE,
                            origin TEXT)""")

    def insert_data_to_urls(self, data: list, origin: str) -> None:
        """Inserts data to the urls table"""
        self._insert_to_table(self.URLS, data, origin)

    def insert_data_to_ip_addresses(self, data: list, origin: str) -> None:
        """Inserts data to the ip_addresses table"""
        self._insert_to_table(self.IP_ADDRESSES, data, origin)

    def _insert_to_table(self, table, address, origin) -> None:
        if address:
            array_origins = [origin] * len(address)
            data = zip(address, array_origins)
            insert = f'INSERT INTO {table} (address, origin) VALUES %s ON CONFLICT (address) DO NOTHING'
            execute_values(self.curs, insert, data)
            print(f"Data from {origin} pushed to DB")

    @exception_handler
    def insert_row(self, table: str, address: str, origin: str) -> None:
        """Inserts single row to the specified table"""
        insert = f'INSERT INTO {table} (address, origin) VALUES (%s, %s) ON CONFLICT (address) DO NOTHING'
        self.curs.execute(insert, (address, origin))

    @exception_handler
    def get_row_by_origin(self, table: str, origin: str) -> list:
        """Return all rows with desired origin from selected table"""
        select = f"SELECT address FROM {table} WHERE origin = %s"
        self.curs.execute(select, (origin,))
        return self.curs.fetchall()

    @exception_handler
    def delete_row_by_origin(self, table: str, origin: str) -> None:
        """Delete all rows with specified origin from selected table"""
        delete = f"DELETE FROM {table} WHERE origin = %s"
        self.curs.execute(delete, (origin,))
