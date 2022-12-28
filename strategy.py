from decimal import Decimal


class StrategyDeal:
    def __init__(self, bank, entry, close, targets):
        self.bank = bank
        self.entry = entry
        self.close = close
        self.targets = targets

    def get_targets(self):
        return self.targets

    def get_target_percents(self):
        tar = list()
        for target in self.get_targets():
            t = round((target / self.entry - 1) * 100, 3)
            tar.append(t)
        return tar

    def get_target_banks(self):
        # список значений банков, если продавать активы по таргетам, как в пример, округленные до 3 знака [1069.12, 1133.764, 1168.573]
        tar1 = list()
        for p in self.get_target_percents():
            num = round(self.bank * (1 + p / 100), 3)
            tar1.append(num)
        return tar1

    def __str__(self):
        template = f"""
BANK: {self.bank}
START_PRICE = {self.entry}
STOP_PRICE = {self.close}

            """

        for i in range(len(self.get_targets())):
            template += f"""
{i + 1} target: {self.get_targets()[i]}
Percent: {self.get_target_percents()[i]}%
Bank: {self.get_target_banks()[i]}

            """

        template += """

----

            """

        return template


def read_data(file_name):
    with open(file_name) as f:
        content = f.read()
    return content


def write_data(file_name, data):
    with open(file_name, "w") as f:
        f.write(data)
    return data


def preprocess(data):
    for line in data.split("\n"):
        if 'Bank:' in line:
            bank = line.split()[-1]
            bank = round(float(Decimal(bank.strip('USD'))), 3)
        elif 'Entry:' in line:
            entry = line.split()[-1]
            entry = round(float(float(Decimal(entry.strip('USD')))), 3)
        elif 'Close:' in line:
            close = line.split()[-1]
            close = round(float(Decimal(close.strip('USD'))), 3)
        elif 'Target:' in line:
            targets = list()
            for target in line.split()[1:]:
                if target[-1] == ';':
                    targets.append(round(float(target[:-4]), 3))
                else:
                    targets.append(round(float(target[:-3]), 3))

    return bank, entry, close, targets


def parse_data(data):
    arr = list()
    for x in data.split('-----'):
        if len(x.strip()) != 0:
            arr.append(x.strip())
    parsed = list()
    for i in arr:
        parsed.append(preprocess(i))

    return parsed


def main():
    content = read_data('deals.txt')
    content = parse_data(content)
    final = str()
    for x in content:
        deal = StrategyDeal(x[0], x[1], x[2], x[3])
        final += deal.__str__()
    write_data('out.txt', final)


if __name__ == '__main__':
    main()
