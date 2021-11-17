class Complex_count:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Complex_count(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"{self.x}+{self.y}i"

    def __mul__(self, other):
        return Complex_count(self.x * other.x - self.y * other.y, self.x * other.y - self.y * other.x)


a = Complex_count(1, 2)
b = Complex_count(3, 4)
print(a + b)
print(a * b)
