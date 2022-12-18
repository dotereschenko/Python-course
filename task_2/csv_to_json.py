import csv
import json


class Converter:

    def __init__(self, csv_path, json_path):
        self.csv_path = csv_path
        self.json_path = json_path

    def read(self):
        with open(self.csv_path, "r", newline="") as csvf:
            return list(csv.DictReader(csvf, delimiter=','))

    def write(self, data):
        data = json.dumps(data)
        with open(self.json_path, "w") as jsonf:
            jsonf.write(data)
        print("Successfully converted!")
        return data

def main():
        csv_path = "./input.csv"
        json_path = "./output.json"
        converter = Converter(csv_path=csv_path, json_path=json_path)

        data = converter.read()
        converter.write(data)

def load_json():
    file_path = './output.json'
    with open(file_path, 'r') as jsonf:
        content = jsonf.read()
        json.loads(content)


if __name__ == '__main__':
    main()
