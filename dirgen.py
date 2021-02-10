import os
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

Directories(['.', './test', './test/subtest', './test/empty', './test/empty/empty2']).write()
Files({'./README.md': '# Generate a directory tree\n\nA weird experiment. A Python file that when run generates a Python file, which when run generates the directory structure, files, and contents of the directory structure the first file was run in. It does this in a very non-transparent way.\n', './dirgengen.py': 'import os\nimport inspect\n\n\nclass Directories(list):\n    def write(self):\n        """\n        create directories for each thing in this object\n        """\n        for d in self:\n            os.makedirs(d, exist_ok=True)\n\n    def describe(self):\n        """\n        Have the object describe how to instantiate itself\n        """\n        return f"Directories({self})"\n\n\nclass Files(dict):\n    def write(self):\n        for name, conts in self.items():\n            with open(name, "w") as f:\n                f.write(conts)\n\n    def describe(self):\n        return f"Files({self})"\n\n\ndef write_gen(txt):\n    with open("dirgen.py", "a") as f:\n        f.write(txt + "\\n")\n\n\ndef build_objects(path):\n    dirs = [dp for dp, _, _ in os.walk(".") if not dp.startswith("./.")]\n    fnames = [os.path.join(dp, f) for dp, _, filenames in os.walk(".")\n            for f in filenames if dp in dirs]\n\n    def contents(name):\n        with open(name) as f:\n            return f.read()\n\n    files = {name : contents(name) for name in fnames}\n    return Directories(dirs), Files(files)\n\n\nif __name__ == "__main__":\n\n    dirs, files = build_objects(".")\n\n    write_gen("import os")\n    write_gen(inspect.getsource(Directories))\n    write_gen(inspect.getsource(Files))\n\n    write_gen(f"{dirs.describe()}.write()")\n    write_gen(f"{files.describe()}.write()")\n', './test/README.md': '# README\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n', './test/subtest/test.txt': '1 2 3 4 5\n6 5 8 9 10\n', './test/subtest/empty.txt': ''}).write()
import os
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

Directories(['.', './test', './test/subtest', './test/empty', './test/empty/empty2']).write()
Files({'./README.md': '# Generate a directory tree\n\nA weird experiment. A Python file that when run generates a Python file, which when run generates the directory structure, files, and contents of the directory structure the first file was run in. It does this in a very non-transparent way.\n', './test/README.md': '# README\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n', './test/subtest/test.txt': '1 2 3 4 5\n6 5 8 9 10\n', './test/subtest/empty.txt': ''}).write()
