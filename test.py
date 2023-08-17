from src.db_model import MyDB
import configparser
import unittest

config = configparser.ConfigParser()
config.read('config.ini')

HOST = config.get('DATABASE', 'host')
PORT = config.get('DATABASE', 'port')
DATABASE = config.get('DATABASE', 'database')
USER = config.get('DATABASE', 'user')
PASSWORD = config.get('DATABASE', 'password')


class TestSQLQueries(unittest.TestCase):

    def test_select_all_employees(self):
        db = MyDB(HOST, int(PORT), DATABASE, USER, PASSWORD)
        address = 'MyURL'
        origin = 'Test'
        expected = "MyURL"
        results = list()
        for table in (db.URLS, db.IP_ADDRESSES):
            db.insert_row(table, address, origin)
            results.append(db.get_row_by_origin(table, origin)[0][0])
            db.delete_row_by_origin(table, origin)
        db.curs.close()
        self.assertEqual(results[0], expected)
        self.assertEqual(results[1], expected)


if __name__ == '__main__':
    unittest.main()
