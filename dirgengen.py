import os
import inspect


class Directories(list):
    def write(self):
        """
        create directories for each thing in this object
        """
        for d in self:
            os.makedirs(d, exist_ok=True)

    def describe(self):
        """
        Have the object describe how to instantiate itself
        """
        return f"Directories({self})"


class Files(dict):
    def write(self):
        for name, conts in self.items():
            with open(name, "w") as f:
                f.write(conts)

    def describe(self):
        return f"Files({self})"


def write_gen(txt):
    with open("dirgen.py", "a") as f:
        f.write(txt + "\n")


def build_objects(path):
    dirs = [dp for dp, _, _ in os.walk(".") if not dp.startswith("./.")]
    fnames = [
        os.path.join(dp, f)
        for dp, _, filenames in os.walk(".")
        for f in filenames
        if dp in dirs and f not in ("dirgen.py", "dirgengen.py")
    ]

    def contents(name):
        with open(name) as f:
            return f.read()

    files = {name: contents(name) for name in fnames}
    return Directories(dirs), Files(files)


if __name__ == "__main__":

    dirs, files = build_objects(".")

    write_gen("import os")
    write_gen(inspect.getsource(Directories))
    write_gen(inspect.getsource(Files))

    write_gen(f"{dirs.describe()}.write()")
    write_gen(f"{files.describe()}.write()")
