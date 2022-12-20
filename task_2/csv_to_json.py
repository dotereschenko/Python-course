import csv
import json

def read(csv_file):
    with open(csv_file, "r", newline="") as csvf:
        return list(csv.DictReader(csvf, delimiter=','))

def write(data,json_file):
    data = json.dumps(data)
    with open(json_file, "w") as jsonf:
        jsonf.write(data)
    return data

def main():
        csv_file = "./input.csv"
        json_file = "./output.json"

        data = read(csv_file)
        write(data,json_file)



if __name__ == '__main__':
    main()
