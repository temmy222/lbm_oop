class FileParser(object):
    def __init__(self, file):
        self.file = file

    def read_file(self):
        with open(self.file) as file:
            line = file.readlines()
        m = self.split_line(line[1])
        print(type(m[1]))

    @staticmethod
    def split_line(value):
        split_value = value.split("(")
        return split_value

