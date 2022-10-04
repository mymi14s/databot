import unittest, os
import main

class TestJsonData(unittest.TestCase):

    def test_get_data(self):
        print("\nTesting if data can be found....\n")
        self.assertEqual(main.get_json(os.getcwd()+'/data/data_1.json').get('found'), True)

    def test_data_type(self):
        print("\nTesting for datatype = dict....\n")
        self.assertEqual(type(main.get_json(os.getcwd()+'/data/data_1.json').get('data')), dict)


if __name__ == '__main__':
    unittest.main()