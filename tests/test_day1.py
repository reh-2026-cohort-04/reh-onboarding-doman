"""Test normal and edge cases for the Day 1 OOP exercises."""

import gc

import pytest

from exercises.day1.accounts_inventory import BankAccount, Inventory, Item
from exercises.day1.objects import (
    Book,
    Car,
    Circle,
    CleanupDemo,
    Date,
    Point,
    Polygon,
    Rectangle,
)
from exercises.day1.people import Employee, Manager, Person, Student, User


def test_bank_account_transactions() -> None:
    account = BankAccount("Bob")
    assert account.owner == "Bob"
    assert account.balance == 0.0

    account.deposit(50)
    account.withdraw(20)
    assert account.balance == 30.0


@pytest.mark.parametrize("amount", [-10.0, 0.0, float("nan")])
def test_invalid_transactions_leave_balance_unchanged(amount: float) -> None:
    account = BankAccount("Bob", 50)

    with pytest.raises(ValueError):
        account.deposit(amount)
    with pytest.raises(ValueError):
        account.withdraw(amount)

    assert account.balance == 50.0


def test_overdraft_leaves_balance_unchanged() -> None:
    account = BankAccount("Bob", 30)

    with pytest.raises(ValueError, match="Insufficient funds"):
        account.withdraw(31)

    assert account.balance == 30.0
    account.withdraw(30)
    assert account.balance == 0.0


def test_inventory_uses_current_item_prices() -> None:
    inventory = Inventory()
    assert inventory.total_value() == 0.0

    pen = Item("Pen", 2)
    inventory.add_item(pen)
    inventory.add_item(Item("Book", 8))
    assert inventory.total_value() == 10.0

    pen.price = 3
    assert inventory.total_value() == 11.0


@pytest.mark.parametrize("price", [-10.0, 0.0, float("inf")])
def test_item_rejects_invalid_prices(price: float) -> None:
    with pytest.raises(ValueError, match="Price must be positive"):
        Item("Pen", price)

    item = Item("Pen", 2)
    with pytest.raises(ValueError, match="Price must be positive"):
        item.price = price

    assert item.price == 2.0


def test_student_inherits_extends_and_compares() -> None:
    student = Student("Jamie", "S123", [90, 80, 70])
    assert isinstance(student, Person)
    assert student.greet() == "Hello, I'm Jamie. My student ID is S123."
    assert student.gpa() == 80.0
    assert student.has_higher_gpa_than(Student("Alex", "S124", [70]))
    assert not student.has_higher_gpa_than(Student("Lee", "S125", [80]))


def test_student_with_no_scores() -> None:
    with pytest.raises(ValueError, match="At least one score"):
        Student("Jamie", "S123", []).gpa()


def test_user_password_and_email_helper() -> None:
    user = User("example-password")

    with pytest.raises(AttributeError):
        getattr(user, "__password")

    assert User.is_valid_email("a@a.com")
    assert not User.is_valid_email("abc")


def test_manager_inherits_and_keeps_own_team() -> None:
    manager = Manager("Jamie")
    employee = Employee("Alex")
    manager.add_employee(employee)

    assert isinstance(manager, Employee)
    assert manager.employees == [employee]
    assert Manager("Lee").employees == []


def test_circle_and_rectangle_areas() -> None:
    circle = Circle(5)
    assert Circle.pi == 3.14159
    assert circle.area() == pytest.approx(78.53975)

    rectangle = Rectangle(4, 5)
    assert isinstance(rectangle, Polygon)
    assert Polygon().area() == 0.0
    assert rectangle.area() == 20
    assert Rectangle(10, 5).get_area() == 50


def test_book_representations() -> None:
    book = Book("1984", "Orwell")
    assert str(book) == "1984 by Orwell"
    assert repr(book) == "Book('1984', 'Orwell')"


def test_date_factory() -> None:
    value = Date.from_string("2026-08-11")
    assert (value.year, value.month, value.day) == (2026, 8, 11)


@pytest.mark.parametrize("value", ["20260811", "2026-02-30"])
def test_date_factory_rejects_invalid_dates(value: str) -> None:
    with pytest.raises(ValueError):
        Date.from_string(value)


def test_car_starts_and_speeds_up() -> None:
    car = Car()
    assert not car.started
    assert car.speed == 0.0

    car.start()
    car.speed_up(30)
    assert car.started
    assert car.speed == 30


def test_point_equality() -> None:
    assert Point(1, 2) == Point(1, 2)
    assert Point(1, 2) != Point(2, 1)
    assert Point(1, 2) != (1, 2)


def test_cleanup_message(capsys: pytest.CaptureFixture[str]) -> None:
    demo = CleanupDemo()
    del demo
    gc.collect()

    assert capsys.readouterr().out == "Object destroyed\n"
