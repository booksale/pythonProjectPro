import random
import math

class ProperFraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self.reduce()  # Reducing the fraction to its simplest form

    def reduce(self):
        gcd_val = math.gcd(self.numerator, self.denominator)  # Finding the greatest common divisor
        self.numerator //= gcd_val
        self.denominator //= gcd_val

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"  # Returning a string representation of the fraction

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator  # Checking if fractions are equal

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator  # Comparing fractions

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)  # Adding fractions

    def __sub__(self, other):
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)  # Subtracting fractions

    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return ProperFraction(new_numerator, new_denominator)  # Multiplying fractions

    def __truediv__(self, other):
        if other.numerator == 0:
            raise ValueError("Division by zero")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return ProperFraction(new_numerator, new_denominator)  # Dividing fractions

# Example usage:
fraction1 = ProperFraction(random.randint(1, 10), random.randint(1, 10))
fraction2 = ProperFraction(random.randint(1, 10), random.randint(1, 10))

print(f"Fraction 1: {fraction1}")
print(f"Fraction 2: {fraction2}")

print(f"Addition: {fraction1} + {fraction2} = {fraction1 + fraction2}")
print(f"Subtraction: {fraction1} - {fraction2} = {fraction1 - fraction2}")
print(f"Multiplication: {fraction1} * {fraction2} = {fraction1 * fraction2}")
print(f"Division: {fraction1} / {fraction2} = {fraction1 / fraction2}")

print(f"fraction1 == fraction2: {fraction1 == fraction2}")
print(f"fraction1 < fraction2: {fraction1 < fraction2}")
