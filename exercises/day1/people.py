"""People, students, users, and managers."""

from __future__ import annotations


class Person:
    """Represent a person with a name."""

    def __init__(self, name: str) -> None:
        self.name = name

    def greet(self) -> str:
        """Return a greeting containing the person's name."""
        return f"Hello, I'm {self.name}."


class Student(Person):
    """Extend a person with a student ID and scores."""

    def __init__(self, name: str, student_id: str, scores: list[float]) -> None:
        super().__init__(name)
        self.student_id = student_id
        self.scores = scores.copy()

    def gpa(self) -> float:
        """Return the mean of the student's scores."""
        if not self.scores:
            raise ValueError("At least one score is required.")
        return sum(self.scores) / len(self.scores)

    def has_higher_gpa_than(self, other: Student) -> bool:
        """Return whether this student's GPA is strictly higher."""
        return self.gpa() > other.gpa()

    def greet(self) -> str:
        """Extend the person's greeting with the student ID."""
        return f"{super().greet()} My student ID is {self.student_id}."


class User:
    """Demonstrate a name-mangled attribute and a static helper."""

    def __init__(self, password: str) -> None:
        self.__password = password

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Check whether the string contains an at-sign."""
        return "@" in email


class Employee:
    """Represent an employee with a name."""

    def __init__(self, name: str) -> None:
        self.name = name


class Manager(Employee):
    """Represent an employee who manages a team."""

    def __init__(self, name: str) -> None:
        super().__init__(name)
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to this manager's team."""
        self.employees.append(employee)
