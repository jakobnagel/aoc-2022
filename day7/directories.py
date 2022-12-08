class Dir:
    def __init__(self, name, parent_dir) -> None:
        self.name = name
        self.parent_dir = parent_dir if parent_dir is not None else self
        self.dirs = []
        self.files = []

    def size(self):
        return sum([f.size for f in self.files]) + sum([d.size() for d in self.dirs])

    def get_dir(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir

    def sum_at_most(self, value):
        total = 0
        if self.size() <= value:
            total += self.size()

        for d in self.dirs:
            total += d.sum_at_most(value)

        return total

    def smallest_dir_free(self, needed_space):
        if self.size() < needed_space:
            return None

        cur_size = self.size()
        for d in self.dirs:
            d_size = d.smallest_dir_free(needed_space)
            if d_size is not None:
                if d_size < cur_size:
                    cur_size = d_size

        return cur_size


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


base = Dir("", None)

commands = open('input.txt')

cur_dir = base

# Loads directories and files
while commands:
    line = commands.readline()
    if line == '':
        break
    if line.startswith('$'):
        command = line.split(' ')[1]
        if command == ('cd'):
            name = line[5:-1]
            if name.startswith('/'):
                cur_dir = base
            elif name.startswith('..'):
                cur_dir = cur_dir.parent_dir
            else:
                cur_dir = cur_dir.get_dir(name)
    elif line.startswith('dir'):
        name = line[4:-1]
        cur_dir.dirs.append(Dir(name, cur_dir))
    else:
        size, name = line.split(' ')
        cur_dir.files.append(File(name, int(size)))


print(base.sum_at_most(100000))

needed_space = 30000000 - (70000000 - base.size())

print(base.smallest_dir_free(needed_space))
