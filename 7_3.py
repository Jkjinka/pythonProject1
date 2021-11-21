class Cell:
    def __init__(self, n):
        self.n = int(n)

    def __str__(self):
        return f"{self.n}"

    def __add__(self, other):
        return Cell(self.n + other.n)

    def __sub__(self, other):
        a = self.n - other.n
        if a > 0:
            return Cell(a)
        else:
            return "Разность количества ячеек меньше нуля!"

    def __mul__(self, other):
        return Cell(self.n * other.n)

    def __truediv__(self, other):
        return Cell(round(self.n / other.n))

    def make_order(self, a):
        b = self.n // a
        for i in range(b):
            c = "*" * a
            print(c)
        c = "*" * (self.n % a)
        print(c)


с1 = Cell(12)
с2 = Cell(10)
с1.make_order(3)
