class StrategyDeal:
    def __init__(self, bank, entry, targets, close):
        self.bank = bank
        self.entry = entry
        self.targets = targets
        self.close = close


    def get_targets(self):
        return self.targets


    def get_target_percents(self):
        tar = list()
        for target in self.get_targets():
            t = round((target / self.entry - 1) * 100, 3)
            tar.append(t)
        return tar

    def get_target_banks(self):
        tar1 = list()
        for p in self.get_target_percents():
            num = round(self.bank * (1 + p / 100), 3)
            tar1.append(num)
        return tar1

    def __str__(self):
        tar = self.get_targets()
        per = self.get_target_percents()
        tb = self.get_target_banks()

        s = f"""
        BANK: {self.bank}
        START_PRICE = {self.entry}
        STOP_PRICE = {self.close}
        
        
            """
        for i in range(len(tar)):
            s += f"""
        {i + 1} target: {tar[i]}
        Percent: {per[i]}%
        Bank: {tb[i]}

                    """

        s += """

        ----

                    """

        return s




def read_data(file_name):
    with open(file_name) as f:
        content = f.read()
    return content



def write_data(file_name, data):
    with open(file_name,'w') as f:
        content = f.write()
    return content




def parse_data(data):
    pass


def main():
    content = read_data('deals.txt')
# content = read_data('deals.txt')
# result = content
# write_data('out.txt', result)


if __name__ == '__main__':
    main()





