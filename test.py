from main import connect_to_database
import unittest


class TestSQLQueries(unittest.TestCase):

    def test_select_all_employees(self):
        db = connect_to_database()
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
