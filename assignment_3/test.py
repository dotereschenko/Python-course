from csv_to_json import Converter
from self_csv_to_json import SelfConverter, convert_row_to_pretty_json
import unittest
import json


class TestCsvJsonConverter(unittest.TestCase):

    csv_path = "./input.csv"
    json_path = "./output.json"
    self_converter = SelfConverter(csv_path, json_path)
    easy_converter = Converter(csv_path, json_path)

    def test_read(self):
        self.assertTrue(self.self_converter.read_data())
        self.assertTrue(self.easy_converter.read())

    def test_write(self):
        data = self.easy_converter.read()
        written_data = self.easy_converter.write(data)

        title, values = self.self_converter.read_data()

        data = convert_row_to_pretty_json(title, values)
        check_data = self.self_converter.write_data(data)
        self.assertEqual(written_data, check_data)

    def test_row_to_pretty(self):
        data = self.easy_converter.read()
        data_lib = json.dumps(data)

        title, values = self.self_converter.read_data()
        data_self = convert_row_to_pretty_json(title, values)
        self.assertEqual(data_lib, data_self)



if __name__ == '__main__':
    unittest.main()