from traceback import extract_tb
from sys import exc_info


def force_load(module_name):
    file_name = module_name + ".py"
    with open(file_name, "r") as file:
        file_lines = file.readlines()
        size = len(file_lines)
        for i in range(size):
            try:
                exec("".join(file_lines), globals())
            except SyntaxError as e:
                file_lines.pop(e.lineno - 1)
            except Exception as e:
                traceback = exc_info()[2:]
                file_lines.pop(extract_tb(*traceback)[-1][1] - 1)
    ldict = {}
    exec("".join(file_lines), globals(), ldict)
    return ldict
