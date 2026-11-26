"""Bank account and inventory exercises."""

from math import isfinite


class BankAccount:
    """Track an owner's balance and validate transactions."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if not isfinite(balance) or balance < 0:
            raise ValueError("Starting balance must be finite and non-negative.")
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        """Add a positive, finite amount to the balance."""
        if not isfinite(amount) or amount <= 0:
            raise ValueError("Deposit amount must be positive and finite.")
        new_balance = self.balance + amount
        if not isfinite(new_balance):
            raise ValueError("Resulting balance must be finite.")
        self.balance = new_balance

    def withdraw(self, amount: float) -> None:
        """Withdraw a positive, finite amount without overdrawing."""
        if not isfinite(amount) or amount <= 0:
            raise ValueError("Withdrawal amount must be positive and finite.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount


class Item:
    """Store an item with a validated price."""

    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price

    @property
    def price(self) -> float:
        """Return the current price."""
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        """Store a positive, finite price."""
        if not isfinite(value) or value <= 0:
            raise ValueError("Price must be positive and finite.")
        self._price = float(value)


class Inventory:
    """Keep a list of items and calculate their total value."""

    def __init__(self) -> None:
        self.items: list[Item] = []

    def add_item(self, item: Item) -> None:
        """Add an item to the inventory."""
        self.items.append(item)

    def total_value(self) -> float:
        """Return the sum of the current item prices."""
        return sum((item.price for item in self.items), 0.0)
