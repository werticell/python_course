from contextlib import contextmanager


class supresser:
    def __init__(self, *type_of_error):
        self.et = type_of_error

    def __enter__(self):
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        for error in self.et:
            if error == exc_type:
                return True


class dumper:
    def __init__(self, stream):
        self.stream = stream

    def __enter__(self):
        return self.stream

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stream.write(str(exc_val))


@contextmanager
def retyper(type_from, type_to):
    try:
        yield
    except type_from as e:
        exeption = type_to()
        exeption.args = e.args
        raise exeption
