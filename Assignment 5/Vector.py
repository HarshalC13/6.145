class Vector:
    def __init__(self, other):
        if isinstance(other, str):
            other = Vector([other])
        if isinstance(other, int):
            other = Vector([other])
        self.array = other

    def as_list(self):
        return self.array

    def size(self):
        return len(self.array)

    def magnitude(self):
        self.mag = []
        total = 0
        for x in self.array:
            self.mag.append(x ** 2)
        for y in self.mag:
            total = total + y
        return total ** .5

    def euclidean_distance(self, other):
        y = 0
        for x in range(len(self.array)):
            y = (self.array[x] - other.array[x]) ** 2 + y
        total = y ** 0.5
        return total

    def normalized(self):
        ans = self.magnitude()
        normalized_list = []
        for x in self.array:
            normalized_list.append(x / ans)
        return Vector(normalized_list)

    def cosine_similarity(self, other):
        a = 0
        ans_1 = self.magnitude()
        ans_2 = other.magnitude()
        b = ans_1 * ans_2
        for x in range(len(self.array)):
            a = a + (self.array[x] * other.array[x])
        cos = a / b
        return cos

    def __add__(self, other):
        add_list = []
        if not isinstance(other, Vector):
            return None
        elif len(self.array) == len(other.array):
            for x in range(len(self.array)):
                y = self.array[x] + other.array[x]
                add_list.append(y)
            return Vector(add_list)
        else:
            return None

    def __sub__(self, other):
        sub_list = []
        if not isinstance(other, Vector):
            return None
        elif len(self.array) == len(other.array):
            for x in range(len(self.array)):
                y = self.array[x] - other.array[x]
                sub_list.append(y)
            return Vector(sub_list)
        else:
            return None

    def __mul__(self, other):
        a = 0
        mul_list = []
        if isinstance(other, int):
            for x in self.array:
                mul_list.append(x * other)
            return Vector(mul_list)
        if isinstance(other, float):
            for x in self.array:
                mul_list.append(x * other)
            return Vector(mul_list)
        if isinstance(other, str):
            return None
        if len(self.array) == len(other.array):
            for x in range(len(self.array)):
                a = a + (self.array[x] * other.array[x])
            return a
        else:
            return None

    def __truediv__(self, other):
        div_list = []
        if other == 0:
            return None
        elif isinstance(other, int):
            for x in self.array:
                div_list.append(x / other)
            return Vector(div_list)
        if isinstance(other, float):
            for x in self.array:
                div_list.append(x / other)
            return Vector(div_list)
        if isinstance(other, str):
            return None
        if len(other.array) == 1:
            for x in self.array:
                div_list.append(x / other.array[0])
            return Vector(div_list)
        if other == 0:
            return None
        else:
            return None