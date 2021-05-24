from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lists):
        result = list()
        for x in lists:
            result.append(x.copy())
        self.lists = result

    def __str__(self):
        result = ''
        for j, new_list in enumerate(self.lists):
            for i, element in enumerate(new_list):
                if i != len(new_list) - 1:
                    result += (str(element) + '\t')
                elif j != len(self.lists) - 1:
                    result += (str(element) + '\n')
                else:
                    result += str(element)
        return result

    def size(self):
        return len(self.lists), len(self.lists[0])  # строки, столбцы

    def __add__(self, other):
        rows, columns = self.size()
        if (rows, columns) != other.size():
            raise MatrixError(self, other)
        result = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                result[i][j] = self.lists[i][j] + other.lists[i][j]
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            rows, columns = self.size()
            result = [[0] * columns for i in range(rows)]
            for i in range(rows):
                for j in range(columns):
                    result[i][j] = self.lists[i][j] * other
            return Matrix(result)
        elif isinstance(other, Matrix):
            rows, columns = self.size()
            rows_other, columns_other = other.size()
            if columns != rows_other:
                raise MatrixError(self, other)
            else:
                result = [[0] * columns_other for i in range(rows)]
                for i in range(rows):
                    for j in range(columns_other):
                        small_res = 0
                        for k in range(columns):
                            small_res += self.lists[i][k] * other.lists[k][j]
                        result[i][j] = small_res
                return Matrix(result)
        else:
            raise TypeError

    __rmul__ = __mul__

    def transpose(self):
        rows, columns = self.size()
        result = [[0] * rows for i in range(columns)]
        for i in range(rows):
            for j in range(columns):
                result[j][i] = self.lists[i][j]

        self.lists = result
        return self

    @staticmethod
    def transposed(matrix):
        rows, columns = matrix.size()
        result = [[0] * rows for i in range(columns)]
        for i in range(rows):
            for j in range(columns):
                result[j][i] = matrix.lists[i][j]

        return Matrix(result)


exec(stdin.read())
