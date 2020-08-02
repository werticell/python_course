import sys


class ExtendedList(list):
    @property
    def reversed(self):
        return self[::-1]

    @property
    def first(self):
        return self[0]

    @first.setter
    def first(self, value):
        self[0] = value

    @property
    def last(self):
        return self[len(self) - 1]

    @last.setter
    def last(self, value):
        self[len(self) - 1] = value

    @property
    def size(self):
        return len(self)

    @size.setter
    def size(self, value):
        size = len(self)
        if value > size:
            for i in range(size, value):
                self.append(None)
        else:
            for i in range(size - 1, value - 1, -1):
                del self[i]

    R = reversed
    F = first
    L = last
    S = size


exec(sys.stdin.read())


