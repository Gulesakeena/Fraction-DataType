from math import gcd


class Fraction:
    def __init__(self, numerator, denominator=1):
        if denominator == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and denominator must be integers.")

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        common = gcd(abs(numerator), abs(denominator))

        self.numerator = numerator // common
        self.denominator = denominator // common

    # -------------------------
    # String Representation
    # -------------------------
    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    # -------------------------
    # Helper
    # -------------------------
    @staticmethod
    def _convert(value):
        if isinstance(value, Fraction):
            return value
        elif isinstance(value, int):
            return Fraction(value)
        else:
            raise TypeError("Operation only supported with Fraction or int.")

    # -------------------------
    # Arithmetic Operators
    # -------------------------
    def __add__(self, other):
        other = self._convert(other)
        num = self.numerator * other.denominator + other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = self._convert(other)
        num = self.numerator * other.denominator - other.numerator * self.denominator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rsub__(self, other):
        other = self._convert(other)
        return other - self

    def __mul__(self, other):
        other = self._convert(other)
        num = self.numerator * other.numerator
        den = self.denominator * other.denominator
        return Fraction(num, den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = self._convert(other)

        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction.")

        num = self.numerator * other.denominator
        den = self.denominator * other.numerator
        return Fraction(num, den)

    def __rtruediv__(self, other):
        other = self._convert(other)
        return other / self

    def __floordiv__(self, other):
        return int((self / other).to_float())

    def __mod__(self, other):
        return self.to_float() % self._convert(other).to_float()

    def __pow__(self, power):
        if not isinstance(power, int):
            raise TypeError("Power must be an integer.")

        if power >= 0:
            return Fraction(self.numerator ** power, self.denominator ** power)
        else:
            return Fraction(self.denominator ** abs(power),
                            self.numerator ** abs(power))

    # -------------------------
    # Unary Operators
    # -------------------------
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __pos__(self):
        return Fraction(self.numerator, self.denominator)

    def __abs__(self):
        return Fraction(abs(self.numerator), self.denominator)

    # -------------------------
    # Comparison Operators
    # -------------------------
    def __eq__(self, other):
        other = self._convert(other)
        return (self.numerator == other.numerator and
                self.denominator == other.denominator)

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        other = self._convert(other)
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        other = self._convert(other)
        return self.numerator * other.denominator <= other.numerator * self.denominator

    def __gt__(self, other):
        other = self._convert(other)
        return self.numerator * other.denominator > other.numerator * self.denominator

    def __ge__(self, other):
        other = self._convert(other)
        return self.numerator * other.denominator >= other.numerator * self.denominator

    # -------------------------
    # Type Conversion
    # -------------------------
    def __float__(self):
        return self.numerator / self.denominator

    def __int__(self):
        return self.numerator // self.denominator

    def __bool__(self):
        return self.numerator != 0

    # -------------------------
    # Container Behavior
    # -------------------------
    def __len__(self):
        return 2

    def __getitem__(self, index):
        if index == 0:
            return self.numerator
        elif index == 1:
            return self.denominator
        else:
            raise IndexError("Fraction index out of range.")

    # -------------------------
    # Hash
    # -------------------------
    def __hash__(self):
        return hash((self.numerator, self.denominator))

    # -------------------------
    # Utility Methods
    # -------------------------
    def reciprocal(self):
        if self.numerator == 0:
            raise ZeroDivisionError("Zero has no reciprocal.")
        return Fraction(self.denominator, self.numerator)

    def simplify(self):
        return Fraction(self.numerator, self.denominator)

    def to_float(self):
        return self.numerator / self.denominator

    def as_tuple(self):
        return (self.numerator, self.denominator)
