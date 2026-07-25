from fraction import Fraction

a = Fraction(1, 2)
b = Fraction(3, 4)

print("a =", a)
print("b =", b)

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Power:", a ** 2)
print("Comparison:", a < b)
print("Reciprocal:", a.reciprocal())
print("Float:", float(a))
print("Tuple:", a.as_tuple())