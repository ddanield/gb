import copy
from abc import ABC, abstractmethod


# problem 1
class Matrix:
    def __init__(self, rows):
        self.m = len(rows)
        self.n = len(rows[0])
        for idx, row in enumerate(rows):
            if len(row) != self.n:
                row_output = ' '.join(map(str, row))
                raise Exception(
                    f'Wrong length of row {idx}: expected {self.n}, actual {len(row)}\n{row_output}'
                )
        self.rows = rows

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'

    def __eq__(self, matrix):
        return matrix.rows == self.rows

    def __add__(self, matrix):
        if self.size != matrix.size:
            raise Exception(f'Cannot get sum of matrices with different sizes {self.size} and {matrix.size}!')

        result = Matrix(copy.deepcopy(self.rows))

        for i in range(self.m):
            for j in range(self.n):
                result[i][j] += matrix[i][j]

        return result

    @property
    def size(self):
        return self.m, self.n


# problem 2
class Clothes(ABC):
    def __init__(self, size):
        try:
            self.size = float(size)
        except ValueError as e:
            print('Size must be a number!')
            raise e

    @abstractmethod
    def calculate_material(self):
        pass


class Coat(Clothes):
    def calculate_material(self):
        return self.size / 6.5 + 0.5


class Suit(Clothes):
    def calculate_material(self):
        return self.size * 2 + 0.3


# problem 3
class Tissue:
    def __init__(self, cells_count):
        cells_count = self.__parse_positive_int(cells_count)
        if cells_count <= 0:
            raise ValueError('Cells count must be a positive integer!')

        self.cells_count = int(cells_count)

    @staticmethod
    def __parse_positive_int(number):
        try:
            number = int(number)
        except ValueError:
            number = 0
        return number

    @staticmethod
    def __check_type(obj):
        if not isinstance(obj, Tissue):
            raise TypeError(f'Object {obj} must be an instance of {Tissue.__class__.__name__} class!')

    def __add__(self, other):
        self.__check_type(other)
        return Tissue(self.cells_count + other.cells_count)

    def __sub__(self, other):
        self.__check_type(other)
        if other.cells_count > self.cells_count:
            raise ValueError('Result of subtraction of cells counts must be greater than 0!')
        return Tissue(self.cells_count - other.cells_count)

    def __mul__(self, other):
        self.__check_type(other)
        return Tissue(self.cells_count * other.cells_count)

    def __floordiv__(self, other):
        self.__check_type(other)
        return Tissue(self.cells_count // other.cells_count)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.cells_count})'

    @classmethod
    def make_order(cls, obj, row_length):
        cls.__check_type(obj)
        row_length = cls.__parse_positive_int(row_length)
        if row_length <= 0:
            raise ValueError('Row length must be a positive integer!')

        return ('*' * row_length + '\n') * (obj.cells_count // row_length) + ('*' * (obj.cells_count % row_length))


if __name__ == '__main__':
    # problem 1
    a = Matrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    b = Matrix([
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ])
    print(a + b)

    # Error
    Matrix([
        [10, 20, 30],
        [40, 50],
    ])
    c = Matrix([
        [10, 20, 30],
        [40, 50, 60],
    ])
    print(a + c)

    # problem 2
    coat = Coat(52.5)
    print(coat.calculate_material())
    suit = Suit('170')
    print(suit.calculate_material())

    # Error
    Suit('asd')
    Clothes(12.5)

    # problem 3
    sample_1 = Tissue(10)
    sample_2 = Tissue(4)
    sample_3 = Tissue(15)

    print(sample_1 + sample_2)
    print(sample_1 - sample_2)
    print(sample_1 * sample_2)
    print(sample_1 // sample_2)

    print('Sample 1, order 4')
    print(Tissue.make_order(sample_1, 4))
    print('Sample 2, order 3')
    print(Tissue.make_order(sample_2, 3))
    print('Sample 3, order 7')
    print(Tissue.make_order(sample_3, 7))

    print('Sample 2, order 10')
    print(Tissue.make_order(sample_2, 10))
    print('Sample 2, order 1')
    print(Tissue.make_order(sample_2, 1))

    # Error
    Tissue(-1)
    Tissue('asd')
    sample_1 - sample_3
