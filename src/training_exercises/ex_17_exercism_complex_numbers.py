"""
Instructions
A complex number is expressed in the form z = a + b * i, where:

a is the real part (a real number),

b is the imaginary part (also a real number), and

i is the imaginary unit satisfying i^2 = -1.

Operations on Complex Numbers
Conjugate
The conjugate of the complex number z = a + b * i is given by:

zc = a - b * i
Absolute Value
The absolute value (or modulus) of z is defined as:

|z| = sqrt(a^2 + b^2)
The square of the absolute value is computed as the product of z and its conjugate zc:

|z|^2 = z * zc = a^2 + b^2
Addition
The sum of two complex numbers z1 = a + b * i and z2 = c + d * i is computed by adding their real and imaginary parts separately:

z1 + z2 = (a + b * i) + (c + d * i)
        = (a + c) + (b + d) * i
Subtraction
The difference of two complex numbers is obtained by subtracting their respective parts:

z1 - z2 = (a + b * i) - (c + d * i)
        = (a - c) + (b - d) * i
Multiplication
The product of two complex numbers is defined as:

z1 * z2 = (a + b * i) * (c + d * i)
        = (a * c - b * d) + (b * c + a * d) * i
Reciprocal
The reciprocal of a non-zero complex number is given by:

1 / z = 1 / (a + b * i)
      = a / (a^2 + b^2) - b / (a^2 + b^2) * i
Division
The division of one complex number by another is given by:

z1 / z2 = z1 * (1 / z2)
        = (a + b * i) / (c + d * i)
        = (a * c + b * d) / (c^2 + d^2) + (b * c - a * d) / (c^2 + d^2) * i
Exponentiation
Raising e (the base of the natural logarithm) to a complex exponent can be expressed using Euler's formula:

e^(a + b * i) = e^a * e^(b * i)
              = e^a * (cos(b) + i * sin(b))
Implementation Requirements
Given that you should not use built-in support for complex numbers, implement the following operations:

addition of two complex numbers
subtraction of two complex numbers
multiplication of two complex numbers
division of two complex numbers
conjugate of a complex number
absolute value of a complex number
exponentiation of e (the base of the natural logarithm) to a complex number

"""

from math import cos, e, isclose, sin


class ComplexNumber:
    """Represents a complex number in the form z = a + b*i.

    A complex number consists of a real part and an imaginary part.
    This class implements standard operations on complex numbers without
    using Python's built-in complex number support.

    Attributes:
        a (float): The real part of the complex number.
        b (float): The imaginary part of the complex number.
    """

    def __init__(self, a: float, b: float):
        """Initialize a complex number with real and imaginary parts.

        Args:
            a (float): The real part of the complex number.
            b (float): The imaginary part of the complex number.
        """
        self.a = a
        self.b = b

    def __repr__(self) -> str:
        """Return a string representation of the complex number.

        Returns:
            str: A string in the format 'a, b' representing a + b*i.
        """
        return f"{self.a}, {self.b}"

    def __eq__(self, other: object) -> bool:
        """Check equality between two complex numbers with tolerance.

        Args:
            other (object): The object to compare with.

        Returns:
            bool: True if both numbers are equal within tolerance, False otherwise.
        """
        if not isinstance(other, ComplexNumber):
            return False
        return isclose(self.a, other.a, abs_tol=1e-9) and isclose(
            self.b, other.b, abs_tol=1e-9
        )

    def conjugate(self) -> "ComplexNumber":
        """Return the complex conjugate of this number.

        The conjugate of z = a + b*i is z* = a - b*i.

        Returns:
            ComplexNumber: The complex conjugate.
        """
        return ComplexNumber(self.a, -self.b)

    def absolute_value(self) -> float:
        """Return the absolute value (modulus) of this complex number.

        The absolute value of z = a + b*i is |z| = sqrt(a^2 + b^2).

        Returns:
            float: The absolute value of the complex number.
        """
        return float((self.a**2 + self.b**2) ** 0.5)

    def addition(self, other: "ComplexNumber") -> "ComplexNumber":
        """Add two complex numbers.

        Args:
            other (ComplexNumber): The complex number to add.

        Returns:
            ComplexNumber: The sum of the two complex numbers.
        """
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def subtraction(self, other: "ComplexNumber") -> "ComplexNumber":
        """Subtract another complex number from this one.

        Args:
            other (ComplexNumber): The complex number to subtract.

        Returns:
            ComplexNumber: The difference of the two complex numbers.
        """
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def multiplication(self, other: "ComplexNumber") -> "ComplexNumber":
        """Multiply two complex numbers.

        Args:
            other (ComplexNumber): The complex number to multiply with.

        Returns:
            ComplexNumber: The product of the two complex numbers.
        """
        return ComplexNumber(
            self.a * other.a - self.b * other.b, self.b * other.a + self.a * other.b
        )

    def reciprocal(self) -> "ComplexNumber":
        """Return the reciprocal (multiplicative inverse) of this complex number.

        The reciprocal of z = a + b*i is 1/z = a/(a^2 + b^2) - b/(a^2 + b^2)*i.

        Returns:
            ComplexNumber: The reciprocal of this complex number.

        Raises:
            ZeroDivisionError: If the complex number is zero.
        """
        return ComplexNumber(
            self.a / (self.a**2 + self.b**2), -self.b / (self.a**2 + self.b**2)
        )

    def division(self, other: "ComplexNumber") -> "ComplexNumber":
        """Divide this complex number by another.

        Args:
            other (ComplexNumber): The complex number to divide by.

        Returns:
            ComplexNumber: The quotient of dividing this by other.

        Raises:
            ZeroDivisionError: If the divisor is zero.
        """
        return ComplexNumber(
            (self.a * other.a + self.b * other.b) / (other.a**2 + other.b**2),
            (self.b * other.a - self.a * other.b) / (other.a**2 + other.b**2),
        )

    def exponential(self) -> "ComplexNumber":
        """Return e raised to the power of this complex number.

        Uses Euler's formula: e^(a + b*i) = e^a * (cos(b) + i*sin(b)).

        Returns:
            ComplexNumber: e raised to the power of this complex number.
        """
        return ComplexNumber(e**self.a * cos(self.b), e**self.a * sin(self.b))
