import os
import inspect


class Directory:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents

    def __repr__(self):
        return self.name

    def add(self, fs):
        self.contents.append(fs)
        return self

    def write(self):
        os.makedirs(self.name, exist_ok=True)
        for content in self.contents:
            content.write()

    def string(self):
        s = f'Directory("{self.name}", [{",".join([f.string() for f in self.contents])}])'
        return s.replace("\\", "")


class File:
    def __init__(self, name, contents=None):
        self.name = name
        self.contents = self.populate() if contents is None else contents

    def __repr__(self):
        return self.name

    def populate(self):
        with open(self.name) as f:
            return f.read()

    def write(self):
        if self.contents == "":
            with open(self.name, "a") as f:
                os.utime(self.name)
        else:
            with open(self.name, "w") as f:
                f.write(self.contents)

    def string(self):
        return f'File("{self.name}", """{self.contents}""")'


def write_gen(txt):
    with open("gen.py", "a") as f:
        f.write(txt + "\n")


def touch(fname):
    with open(fname, "w") as f:
        os.utime(fname)


def build_tree(root):

    tree = Directory(root, [])
    for dname, subdirs, fs in os.walk(root):
        tree.add(
            Directory(
                dname,
                [
                    File(f"{dname}/{f}")
                    for f in fs
                    if f != "dirgen.py" and f != "gen.py"
                ],
            )
        )
    return tree


if __name__ == "__main__":

    directory = build_tree(".")
    touch("gen.py")

    # write out boiler plate objects
    write_gen("import os")
    write_gen(inspect.getsource(Directory))
    write_gen(inspect.getsource(File))
    write_gen(f"{directory.string()}.write()")
