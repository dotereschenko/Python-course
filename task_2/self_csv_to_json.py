def preprocess(data):
    delimeter=","
    title = data.pop(0).strip().split(delimeter)
    return title, data


def to_json(title, values):
    res = list()
    for current_values in values:
        current_dict = dict(zip(title, current_values.split(",")))
        pl = "{"
        current = []
        for key in current_dict:
            current.append('"{key}": "{value}"'.format(key=key, value=current_dict[key]))

        pl += ", ".join(current) + "}"
        res.append(pl)

    res = "[" + ", ".join(res) + "]"
    return res

def read_file(csv_file):
    with open(csv_file, "r", newline="") as f:
        content = f.read().splitlines()
        f.close()
    return preprocess(content)

def write(json_file,data):
    with open(json_file, "w") as f:
        f.write(data)
    return data


if __name__ == "__main__":
    csv_file = "./input.csv"
    json_file = "./output.json"
    title, values = read_file(csv_file)
    data = to_json(title, values)
    write(json_file,data)