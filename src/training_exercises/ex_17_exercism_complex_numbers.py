import math
from math import cos, e, sin


class ComplexNumber:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        return f"{self.a}, {self.b}"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ComplexNumber):
            return False
        return math.isclose(self.a, other.a, abs_tol=1e-9) and math.isclose(
            self.b, other.b, abs_tol=1e-9
        )

    def conjugate(self) -> "ComplexNumber":
        return ComplexNumber(self.a, -self.b)

    def absolute_value(self) -> float:
        return float((self.a**2 + self.b**2) ** 0.5)

    def addition(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def subtraction(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def multiplication(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b
        )

    def reciprocal(self) -> "ComplexNumber":
        return ComplexNumber(
            self.a / (self.a**2 + self.b**2), -self.b / (self.a**2 + self.b**2)
        )

    def division(self, other: "ComplexNumber") -> "ComplexNumber":
        return ComplexNumber(
            (self.a * other.a + self.b * other.b) / (other.a**2 + other.b**2),
            (self.b * other.a - self.a * other.b) / (other.a**2 + other.b**2),
        )

    def exponential(self) -> "ComplexNumber":
        return ComplexNumber(e**self.a * cos(self.b), e**self.a * sin(self.b))


print(ComplexNumber(1, 2).conjugate())
