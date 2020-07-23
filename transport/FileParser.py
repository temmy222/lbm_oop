class FileParser(object):
    def __init__(self, file):
        self.file = file
        self.line = self.read_file()

    def read_file(self):
        with open(self.file) as file:
            line = file.readlines()
        return line
        m = self.get_value(line[4])
        print(m)


    @staticmethod
    def split_line(value, sep):
        split_value = value.split(sep)
        return split_value

    def get_value(self, value):
        initial_split = self.split_line(value, "(")[1]
        last_split = self.split_line(initial_split, ")")[0]
        return last_split

    @property
    def xLength(self):
        full_value = self.get_value(self.line[1])
        value = self.split_line(full_value, ",")[0]
        return value

    @property
    def yLength(self):
        full_value = self.get_value(self.line[1])
        value = self.split_line(full_value, ",")[1]
        return value

    @property
    def latticeType(self):
        value = self.get_value(self.line[2])
        return value

    @property
    def transportType(self):
        value = self.get_value(self.line[3])
        return value

    @property
    def velocity(self):
        value = self.get_value(self.line[4])
        return value

    @property
    def velocity(self):
        value = self.get_value(self.line[4])
        return value

    @property
    def diffusion_coefficient(self):
        value = self.get_value(self.line[4])
        return value


