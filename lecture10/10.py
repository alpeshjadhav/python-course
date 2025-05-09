class MyComplex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return MyComplex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return MyComplex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}j"


a = MyComplex(3, 2)
b = MyComplex(1, 7)

print("a + b =", a + b)      # (4 + 9j)
print("a * b =", a * b)      # (-11 + 23j)
