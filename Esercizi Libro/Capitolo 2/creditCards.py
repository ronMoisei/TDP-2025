from typing import Union


class CreditCard:
    def __init__(self, customer: int, bank: str, acnt: str, limit: float, balance: float):
        self._customer = customer
        self._bank = bank
        self._acnt = acnt
        self._limit = limit
        self._balance = balance


    @property
    def customer(self) -> int:
        return self._customer
    @property
    def bank(self) -> str:
        return self._bank
    @property
    def acnt(self) -> str:
        return self._acnt
    @property
    def limit(self) -> float:
        return self._limit
    @property
    def balance(self) -> float:
        return self._balance

    @customer.setter
    def customer(self):
        if not isinstance(self._customer, int) or self._customer < 0:
            raise ValueError("Customer must be a positive integer")
        return self._customer
    @bank.setter
    def bank(self):
        if not isinstance(self._bank, str):
            raise ValueError("Bank must be a string")
        return self._bank
    @acnt.setter
    def acnt(self):
        if not isinstance(self._acnt, str):
            raise ValueError("Account must be a string")
        return self._acnt
    @limit.setter
    def limit(self, limit: Union[float, int]):
        if not isinstance(self._limit, (float, int)) or self._limit < 0:
            raise ValueError("Limit must be a positive number")
        return self._limit
    @balance.setter
    def balance(self):
        if not isinstance(self._limit, (float, int)):
            raise ValueError("Balance must be a number")
        return self._balance

    def charge(self, price: float):
        if price + self._balance > self._limit:
            return "Exceed limit"
        self._balance += price

    def make_payment(self, payment):
        if self._balance - payment > 0 and payment > 0:
            self._balance -= payment
        else:
            raise ValueError("Payment must be positive")

if __name__ == '__main__':
    c = CreditCard(000000, "Trade Republic", "AAAA-BBBB-CCCC", 1000)
    print(c.balance)
    c.charge(100)
    print(c.balance)