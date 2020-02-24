class Rational:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def computeGCD(self):
        x = self.num
        y = self.den
        while (y):
            x, y = y, x % y
        return x

    def get_numerator(self):
        return int(self.num)

    def get_denominator(self):
        return int(self.den)

    def to_float(self):
        return float(self.num / self.den)

    def reciprocal(self):
        return Rational(self.get_denominator(), self.get_numerator())

    def reduce(self):
        gcd = self.computeGCD()
        reducedRat = Rational(int(self.num / gcd), int(self.den / gcd))
        return reducedRat

    def fracadd(self, other):
        a = self.get_numerator()
        b =self.get_denominator()
        temp = self.get_denominator()
        if isinstance(other, Rational):
            c = other.get_numerator()
            d = other.get_denominator()
            a = a * d
            b = b * d
            c = c * temp
            d = d * temp
            num = a + c
            den = b
            return Rational(num, den)
        elif isinstance(other, int):
            c = other
            d = 1
            a = a * d
            b = b * d
            c = c * temp
            d = d * temp
            num = a + c
            den = b
            return Rational(num, den)


    def __add__(self, other):
        if isinstance(other, Rational) or isinstance(other, int):
            newRat = self.fracadd(other)
            return newRat
        elif isinstance(other, float):
            return (self.get_numerator() / self.get_denominator()) + other
        else:
            return None

    def fracsub(self, other):
        a = self.get_numerator()
        b =self.get_denominator()
        temp = self.get_denominator()
        if isinstance(other, Rational):
            c = other.get_numerator()
            d = other.get_denominator()
            a = a * d
            b = b * d
            c = c * temp
            d = d * temp
            num = a - c
            den = b
            return Rational(num, den)
        elif isinstance(other, int):
            c = other
            d = 1
            a = a * d
            b = b * d
            c = c * temp
            d = d * temp
            num = a - c
            den = b
            return Rational(num, den)


    def __sub__(self, other):
        if isinstance(other, Rational) or isinstance(other, int):
            subRat = self.fracsub(other)
            return subRat
        elif isinstance(other, float):
            return (self.get_numerator() / self.get_denominator()) - other
        else:
            return None

    def __mul__(self, other):
        if isinstance(other, Rational):
            top = self.get_numerator() * other.get_numerator()
            bot = self.get_denominator() * other.get_denominator()
            return Rational(top, bot)
        elif isinstance(other, int):
            top = self.get_numerator() * other
            bot = self.get_denominator() * 1
            return Rational(top, bot)
        elif isinstance(other, float):
            return (self.get_numerator() / self.get_denominator()) * other
        else:
            return None
    def __truediv__(self,other):
        if isinstance(other, Rational):
            other_flipped = other.reciprocal()
            top = self.get_numerator() * other_flipped.get_numerator()
            bot = self.get_denominator() * other_flipped.get_denominator()
            return Rational(top, bot)
        elif isinstance(other, int):
            top = self.get_numerator() * 1
            bot = self.get_denominator() * other
            return Rational(top, bot)
        elif isinstance(other, float):
            return (self.get_numerator() / self.get_denominator()) / other
        else:
            return None

