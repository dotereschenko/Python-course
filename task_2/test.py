import csv_to_json
import self_csv_to_json
import unittest
import json


class TestCsvJsonConverter(unittest.TestCase):

    csv_path = "./input.csv"
    json_path = "./output.json"

    def test_read(self):
        csv_file = "./input.csv"
        self.assertTrue(self_csv_to_json.read_file(csv_file))
        self.assertTrue(csv_to_json.read(csv_file))

    def test_write(self):
        csv_file = "./input.csv"
        json_file = "./output.json"
        data = csv_to_json.read(csv_file)
        written_data = csv_to_json.write(data,json_file)
        title, values = self_csv_to_json.read_file(csv_file)
        data = self_csv_to_json.to_json(title, values)
        check_data = self_csv_to_json.write(json_file,data)
        self.assertEqual(written_data, check_data)


    def test_row_to_pretty(self):
        csv_file = "./input.csv"
        json_file = "./output.json"
        data = csv_to_json.read(csv_file)
        lib = json.dumps(data)
        title, values = self_csv_to_json.read_file(csv_file)
        dself = self_csv_to_json.to_json(title, values)
        self.assertEqual(lib, dself)



if __name__ == '__main__':
    unittest.main()