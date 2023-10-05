import enum
from typing import Protocol


class PaymentStrategyFn(Protocol):
    def __call__(self, amount: int) -> None:
        pass


class PaymentStrategyFactoryFn(Protocol):
    def __call__(self) -> PaymentStrategyFn:
        pass


def cash_payment_strategy(amount: int) -> None:
    print(f"Paid {amount} with cash")


def credit_card_payment_strategy(amount: int) -> None:
    print(f"Paid {amount} with credit card")


def debit_card_payment_strategy(amount: int) -> None:
    print(f"Paid {amount} with debit card")


def paypal_payment_strategy(amount: int) -> None:
    print(f"Paid {amount} with PayPal")


def bank_transfer_payment_strategy(amount: int) -> None:
    print(f"Paid {amount} with bank transfer")


def credit_card_payment_strategy_factory() -> PaymentStrategyFn:
    return credit_card_payment_strategy


def debit_card_payment_strategy_factory() -> PaymentStrategyFn:
    return debit_card_payment_strategy


def bank_transfer_payment_strategy_factory() -> PaymentStrategyFn:
    return bank_transfer_payment_strategy


def cash_payment_strategy_factory() -> PaymentStrategyFn:
    return cash_payment_strategy


def paypal_payment_strategy_factory() -> PaymentStrategyFn:
    return paypal_payment_strategy


class AvailablePaymentStrategyMethods(enum.StrEnum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"


def read_payment(payment_method: AvailablePaymentStrategyMethods) -> PaymentStrategyFn:
    available_methods = {
        "credit_card": credit_card_payment_strategy_factory,
        "debit_card": debit_card_payment_strategy_factory,
        "paypal": paypal_payment_strategy_factory,
        "bank_transfer": bank_transfer_payment_strategy_factory,
        "cash": cash_payment_strategy_factory,
    }

    return available_methods[payment_method]()


class PaymentStrategyContext:
    def __init__(self, payment_strategy_fn: PaymentStrategyFn) -> None:
        self.__payment_strategy_fn = payment_strategy_fn

    def make_payment(self, amount: int) -> None:
        self.__payment_strategy_fn(amount=amount)

    @property
    def payment_strategy(self) -> PaymentStrategyFn:
        return self.__payment_strategy_fn

    @payment_strategy.setter
    def payment_strategy(self, new_payment_strategy: PaymentStrategyFn) -> None:
        self.__payment_strategy_fn = new_payment_strategy


def main() -> None:
    credit_card_strategy: PaymentStrategyFn = read_payment(
        AvailablePaymentStrategyMethods.CREDIT_CARD
    )

    paypal_strategy: PaymentStrategyFn = read_payment(
        AvailablePaymentStrategyMethods.PAYPAL
    )

    cash_strategy: PaymentStrategyFn = read_payment(
        AvailablePaymentStrategyMethods.CASH
    )

    bank_transfer_strategy: PaymentStrategyFn = read_payment(
        AvailablePaymentStrategyMethods.BANK_TRANSFER
    )

    payment_context: PaymentStrategyContext = PaymentStrategyContext(cash_strategy)

    payment_context.make_payment(amount=100)

    payment_context.payment_strategy = paypal_strategy
    payment_context.make_payment(amount=200)

    payment_context.payment_strategy = credit_card_strategy
    payment_context.make_payment(amount=300)

    payment_context.payment_strategy = bank_transfer_strategy
    payment_context.make_payment(amount=400)


if __name__ == "__main__":
    main()
