import random
import json

class Paid:

    def get(self,file):
        date = str(file['year']) + file['month'].strip()
        salary = int(file['salary'])

        if file.get(date):
            file['hour_income'] = file.get(date)
            return json.dumps(file)
        else:
            days = random.randint(20,23)
            per_h = '{:.2f}'.format(salary/(days*8))
            file['hour_income'] = per_h
            return json.dumps(file,indent=2)

def write(data,json_file):
    with open(json_file, "w") as jsonf:
        jsonf.write(data)
    return data

def main():
    s = Paid()
    f = open('input.json')
    data = json.load(f)
    converted=s.get(data)
    print(converted)
    write(converted,'output.json')



if __name__ == '__main__':
    main()