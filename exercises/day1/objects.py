"""Shapes, books, dates, cars, points, and object cleanup."""

import re
from datetime import date
from types import NotImplementedType
from typing import Self


class Circle:
    """Represent a circle using a shared value of pi."""

    pi = 3.14159

    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        """Return the circle's area."""
        return self.pi * self.radius**2


class Book:
    """Store a title and author with two string representations."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    def __str__(self) -> str:
        """Return a readable book description."""
        return f"{self.title} by {self.author}"

    def __repr__(self) -> str:
        """Return a representation showing the constructor arguments."""
        return f"Book({self.title!r}, {self.author!r})"


class Polygon:
    """Provide a base area method for the exercise."""

    def area(self) -> float:
        """Return the default area."""
        return 0.0


class Rectangle(Polygon):
    """Represent a rectangle with a width and height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        """Return width multiplied by height."""
        return self.width * self.height

    def get_area(self) -> float:
        """Return the rectangle's area."""
        return self.area()


class Date:
    """Represent a valid calendar date."""

    def __init__(self, year: int, month: int, day: int) -> None:
        value = date(year, month, day)
        self.year = value.year
        self.month = value.month
        self.day = value.day

    @classmethod
    def from_string(cls, value: str) -> Self:
        """Create a date from a YYYY-MM-DD string."""
        if re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", value) is None:
            raise ValueError("Date must use YYYY-MM-DD format.")
        parsed = date.fromisoformat(value)
        return cls(parsed.year, parsed.month, parsed.day)


class Car:
    """Simulate starting a car and increasing its speed."""

    def __init__(self) -> None:
        self.started = False
        self.speed = 0.0

    def start(self) -> None:
        """Mark the car as started."""
        self.started = True

    def speed_up(self, amount: float) -> None:
        """Increase the car's speed by a non-negative amount."""
        if amount < 0:
            raise ValueError("Speed increase must be non-negative.")
        self.speed += amount


class Point:
    """Represent a two-dimensional point."""

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __eq__(self, other: object) -> bool | NotImplementedType:
        """Compare coordinates when the other object is also a point."""
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)


class CleanupDemo:
    """Demonstrate the destructor requested in the exercise."""

    def __del__(self) -> None:
        """Print a message when Python finalises the object."""
        print("Object destroyed")
