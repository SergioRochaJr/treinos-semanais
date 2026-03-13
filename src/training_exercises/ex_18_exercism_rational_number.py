"""
A rational number is defined as the quotient of two integers a and b, called the numerator and denominator, respectively, where b != 0.

Note
Note that mathematically, the denominator can't be zero. However in many implementations of rational numbers, you will find that the denominator is allowed to be zero with behaviour similar to positive or negative infinity in floating point numbers. In those cases, the denominator and numerator generally still can't both be zero at once.

The absolute value |r| of the rational number r = a/b is equal to |a|/|b|.

The sum of two rational numbers r₁ = a₁/b₁ and r₂ = a₂/b₂ is r₁ + r₂ = a₁/b₁ + a₂/b₂ = (a₁ * b₂ + a₂ * b₁) / (b₁ * b₂).

The difference of two rational numbers r₁ = a₁/b₁ and r₂ = a₂/b₂ is r₁ - r₂ = a₁/b₁ - a₂/b₂ = (a₁ * b₂ - a₂ * b₁) / (b₁ * b₂).

The product (multiplication) of two rational numbers r₁ = a₁/b₁ and r₂ = a₂/b₂ is r₁ * r₂ = (a₁ * a₂) / (b₁ * b₂).

Dividing a rational number r₁ = a₁/b₁ by another r₂ = a₂/b₂ is r₁ / r₂ = (a₁ * b₂) / (a₂ * b₁) if a₂ is not zero.

Exponentiation of a rational number r = a/b to a non-negative integer power n is r^n = (a^n)/(b^n).

Exponentiation of a rational number r = a/b to a negative integer power n is r^n = (b^m)/(a^m), where m = |n|.

Exponentiation of a rational number r = a/b to a real (floating-point) number x is the quotient (a^x)/(b^x), which is a real number.

Exponentiation of a real number x to a rational number r = a/b is x^(a/b) = root(x^a, b), where root(p, q) is the qth root of p.

Implement the following operations:

addition, subtraction, multiplication and division of two rational numbers,
absolute value, exponentiation of a given rational number to an integer power, exponentiation of a given rational number to a real (floating-point) power, exponentiation of a real number to a rational number.
Your implementation of rational numbers should always be reduced to lowest terms. For example, 4/4 should reduce to 1/1, 30/60 should reduce to 1/2, 12/8 should reduce to 3/2, etc. To reduce a rational number r = a/b, divide a and b by the greatest common divisor (gcd) of a and b. So, for example, gcd(12, 8) = 4, so r = 12/8 can be reduced to (12/4)/(8/4) = 3/2. The reduced form of a rational number should be in "standard form" (the denominator should always be a positive integer). If a denominator with a negative integer is present, multiply both numerator and denominator by -1 to ensure standard form is reached. For example, 3/-4 should be reduced to -3/4

Assume that the programming language you are using does not have an implementation of rational numbers.


"""


class RationalNumber:
    """A rational number stored in (numerator/denominator) reduced form.

    The rational number is normalized such that the denominator is always positive
    and the numerator/denominator pair is in lowest terms (their greatest common
    divisor is 1).
    """

    def __init__(self, numerator: int, denominator: int):
        """Initialize a new rational number.

        Args:
            numerator: The numerator of the rational number.
            denominator: The denominator of the rational number. Must not be 0.

        Raises:
            ValueError: If `denominator` is 0.
        """
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        gcd = self.greatest_common_divisor(abs(numerator), abs(denominator))
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self) -> str:
        """Return a string representation of the rational number."""
        return f"{self.numerator}/{self.denominator}"

    def __eq__(self, other: object) -> bool:
        """Compare two rational numbers for equality."""
        if not isinstance(other, RationalNumber):
            return False
        return (
            self.numerator == other.numerator and self.denominator == other.denominator
        )

    def greatest_common_divisor(self, a: int, b: int) -> int:
        """Return the greatest common divisor of a and b using Euclid's algorithm."""
        while b != 0:
            a, b = b, a % b
        return a

    def absolute_value(self) -> "RationalNumber":
        """Return the absolute value of this rational number."""
        return RationalNumber(abs(self.numerator), self.denominator)

    def sum(self, other: "RationalNumber") -> "RationalNumber":
        """Return the sum of this rational number and another."""
        return RationalNumber(
            self.numerator * other.denominator + other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def difference(self, other: "RationalNumber") -> "RationalNumber":
        """Return the difference between this rational number and another."""
        return RationalNumber(
            self.numerator * other.denominator - other.numerator * self.denominator,
            self.denominator * other.denominator,
        )

    def product(self, other: "RationalNumber") -> "RationalNumber":
        """Return the product of this rational number and another."""
        return RationalNumber(
            self.numerator * other.numerator, self.denominator * other.denominator
        )

    def divide(self, other: "RationalNumber") -> "RationalNumber":
        """Divide this rational number by another.

        Raises:
            ValueError: If attempting to divide by zero.
        """
        if other.numerator == 0:
            raise ValueError("Cannot divide by zero.")
        return RationalNumber(
            self.numerator * other.denominator, self.denominator * other.numerator
        )

    def exponentiate(self, n: int) -> "RationalNumber":
        """Raise this rational number to an integer power."""
        return RationalNumber(self.numerator**n, self.denominator**n)

    def negative_exponential(self, n: int) -> "RationalNumber":
        """Raise this rational number to a negative integer power."""
        if self.numerator == 0:
            raise ValueError("Cannot raise zero to a negative power.")
        m = abs(n)
        return RationalNumber(self.denominator**m, self.numerator**m)

    def floating_point_exponentiation(self, x: float) -> float:
        """Raise this rational number to a floating-point power."""
        return float(self.numerator**x / self.denominator**x)

    def exp_real_base(self, base: float) -> float:
        """Raise a real number to this rational power."""
        return float(base ** (self.numerator / self.denominator))
