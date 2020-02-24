import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance_to_origin(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def euclidean_distance(self, other):
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def angle_between(self, other):
        vert = other.y - self.y
        horiz = other.x - self.x
        return math.atan2(vert, horiz)


class Triangle(Point):
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def side_lengths(self):
        sl12 = self.p1.euclidean_distance(self.p2)
        sl23 = self.p2.euclidean_distance(self.p3)
        sl31 = self.p3.euclidean_distance(self.p1)
        return (sl12, sl23, sl31)

    def LawCosines(self, a, b, c):
        return math.acos((c ** 2 - b ** 2 - a ** 2) / (-2.0 * a * b))

    def angles(self):
        a = self.side_lengths()[0]
        b = self.side_lengths()[1]
        c = self.side_lengths()[2]
        a1 = self.LawCosines(a, b, c)
        a2 = self.LawCosines(a, c, b)
        a3 = self.LawCosines(c, b, a)
        return(a1, a2, a3)

    def side_classification(self):
        self.count = 0
        self.comp = self.angles()[0]
        for i in range(1, 3):
            if math.isclose(self.comp, self.angles()[i], rel_tol = 1e-6):
                self.count += 1
        if self.count == 0:
            return "scalene"
        elif self.count == 1:
            return "isosceles"
        else:
            return "equilateral"

    def angle_classification(self):
        a = sorted(self.side_lengths())
        print(a)
        if self.side_classification() == "equilateral":
            return "equiangular"
        elif math.isclose(a[0] ** 2 + a[1] ** 2, a[2] ** 2, rel_tol=1e-6):
            return "right"
        elif (a[0] ** 2 + a[1] ** 2) < a[2] ** 2:
            return "obtuse"
        else:
            return "acute"

    def is_right(self):
        if self.angle_classification() == "right":
            return True
        else:
            return False

    def perimeter(self):
        return (self.side_lengths()[0] + self.side_lengths()[1] + self.side_lengths()[2])

    def area(self):
        p = self.perimeter()
        p = p / 2
        area = math.sqrt(p * (p - self.side_lengths()[0]) * (p - self.side_lengths()[1]) * (p - self.side_lengths()[2]))
        return area
