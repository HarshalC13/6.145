class Matrix:
    def __init__(self, nested):
        self.nested = nested

    def size(self):
        numrows = len(self.nested)
        numcols = len(self.nested[0])
        return (numrows, numcols)

    def get(self, r, c):
        return self.nested[r][c]

    def set(self, r, c, val):
        self.nested[r][c] = val

    def row(self, n):
        return self.nested[n]

    def col(self, n):
        col = [self.nested[i][n] for i in range(len(self.nested))]
        return col

    def transpose(self):
        transpose = [[self.nested[j][i] for j in range(len(self.nested))] for i in range(len(self.nested[0]))]
        return Matrix(transpose)

    def add(self, other):
        if isinstance(other, Matrix) and self.size() == other.size():
            added = [[self.nested[i][j] + other.nested[i][j] for j in range(len(self.nested[0]))] for i in range(len(self.nested))]
            return Matrix(added)
        elif isinstance(other, Matrix):
            return None
        elif isinstance(other, int) or isinstance(other, float):
            added = [[self.nested[i][j] + other for j in range(len(self.nested[0]))] for i in range(len(self.nested))]
            return Matrix(added)
        else:
            return None

    def sub(self, other):
        if isinstance(other, Matrix) and self.size() == other.size():
            subb = [[self.nested[i][j] - other.nested[i][j] for j in range(len(self.nested[0]))] for i in range(len(self.nested))]
            return Matrix(subb)
        elif isinstance(other, Matrix):
            return None
        elif isinstance(other, int) or isinstance(other, float):
            subb = [[self.nested[i][j] - other for j in range(len(self.nested[0]))] for i in range(len(self.nested))]
            return Matrix(subb)
        else:
            return None

    def mul(self, other):
        if isinstance(other, Matrix) and self.size()[1] == other.size()[0]:
            c = [[0 for j in range(len(other.nested[0]))] for i in range(len(self.nested))]
            for i in range(len(self.nested)):
                for j in range(len(other.nested[0])):
                    for k in range(len(other.nested)):
                        c[i][j] += self.nested[i][k] * other.nested[k][j]
            return Matrix(c)
        elif isinstance(other, Matrix):
            return None
        elif isinstance(other, int) or isinstance(other, float):
            mul = [[self.nested[i][j] * other for j in range(len(self.nested[0]))] for i in range(len(self.nested))]
            return Matrix(mul)
        else:
            return None

    def __add__(self, other):
        return self.add(other)

    def __sub__(self, other):
        return self.sub(other)

    def __mul__(self, other):
        return self.mul(other)
