

class Dir(object):

    def __init__(self, name, parent=None):
        self.name = name
        self.children = {}
        self.files = {}
        self.parent = parent

    def child(self, name):
        return self.children[name]

    def add_child(self, name):
        self.children[name] = Dir(name, self)

    def add_file(self, name, size):
        self.files[name] = int(size)

    def calc_dir_file_size(self):
        return sum([v for (k, v) in self.files.items()])

    def calc_dir_total_size(self, max=None):
        dirs_total = {k: v.calc_dir_total_size() for (k, v) in self.children.items()}
        dirs_sum = sum([v for (k, v) in dirs_total.items()])
        dir_total = dirs_sum + self.calc_dir_file_size()
        return dir_total

    def is_root(self):
        return self.parent is None

    def dir_full_path(self):
        return "" if self.is_root() else self.parent.dir_full_path() + "/" + self.name

    def goto_root(self):
        return self if self.is_root() else self.parent.goto_root()

    def walk_full_tree(self):
        entries = []
        self_entry = (self.dir_full_path(), self.calc_dir_total_size())
        entries.append(self_entry)
        if len(self.children) != 0:
            for (child_name, child) in self.children.items():
                entries.extend(child.walk_full_tree())
        return entries


def input_or_output(s):
    return "input" if s[0] == "$" else "output"

def parse_user_input(s):
    command = s[2:4]
    target = s[5:] if command == "cd" else None
    return (command, target)

def parse_output(s):
    tokens = s.split(" ")
    is_dir = tokens[0] == "dir"
    name = tokens[1]
    return (("dir", name), None) if is_dir else (("file", name), tokens[0])