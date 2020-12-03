class data_read:
    def __init__(self, separator):
        self.separator = separator
    def read(self, file):
        data = None
        with open(file) as f:
            if self.separator == 0:
                data = f.read().splitlines()

        return data

    def data_array_to_int(self, array):
        int_list = [int(x) for x in array]
        return int_list
