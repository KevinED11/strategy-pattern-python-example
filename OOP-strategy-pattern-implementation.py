import abc
import enum


class PaymentStrategy(abc.ABC):
    @abc.abstractmethod
    def pay(self, amount: int) -> None:
        pass


class CashPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with cash")


class CreditCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with credit card")


class DebitCardPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with debit card")


class PayPalPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with PayPal")


class BankTransferPaymentStrategy(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with bank transfer")


class PaymentStrategyFactory(abc.ABC):
    @abc.abstractmethod
    def get_payment_strategy(self) -> PaymentStrategy:
        pass


class CreditCardPaymentStrategyFactory(PaymentStrategyFactory):
    def get_payment_strategy(self) -> PaymentStrategy:
        return CreditCardPaymentStrategy()


class DebitCardPaymentStrategyFactory(PaymentStrategyFactory):
    def get_payment_strategy(self) -> PaymentStrategy:
        return DebitCardPaymentStrategy()


class BankTransferPaymentStrategyFactory(PaymentStrategyFactory):
    def get_payment_strategy(self) -> PaymentStrategy:
        return BankTransferPaymentStrategy()


class CashPaymentStrategyFactory(PaymentStrategyFactory):
    def get_payment_strategy(self) -> PaymentStrategy:
        return CashPaymentStrategy()


class PayPalPaymentStrategyFactory(PaymentStrategyFactory):
    def get_payment_strategy(self) -> PaymentStrategy:
        return PayPalPaymentStrategy()


class AvailablePaymentStrategyMethods(enum.StrEnum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"


def read_payment(payment_method: AvailablePaymentStrategyMethods) -> PaymentStrategyFactory:
    available_methods = {
        "credit_card": CreditCardPaymentStrategyFactory(),
        "debit_card": DebitCardPaymentStrategyFactory(),
        "paypal": PayPalPaymentStrategyFactory(),
        "bank_transfer": BankTransferPaymentStrategyFactory(),
        "cash": CashPaymentStrategyFactory(),
    }

    return available_methods[payment_method]


class PaymentStrategyContext:
    def __init__(self, payment_strategy: PaymentStrategy) -> None:
        self.__payment_strategy = payment_strategy

    def make_payment(self, amount: int) -> None:
        self.__payment_strategy.pay(amount=amount)

    @property
    def payment_strategy(self) -> PaymentStrategy:
        return self.__payment_strategy

    @payment_strategy.setter
    def payment_strategy(self, new_payment_strategy: PaymentStrategy) -> None:
        self.__payment_strategy = new_payment_strategy


class Main:
    @staticmethod
    def run() -> None:
        credit_card_payment_strategy = read_payment(
            AvailablePaymentStrategyMethods.CREDIT_CARD
        ).get_payment_strategy()

        paypal_payment_strategy = read_payment(
            AvailablePaymentStrategyMethods.PAYPAL
        ).get_payment_strategy()

        cash_payment_strategy = read_payment(
            AvailablePaymentStrategyMethods.CASH
        ).get_payment_strategy()

        bank_transfer_payment_strategy = read_payment(
            AvailablePaymentStrategyMethods.BANK_TRANSFER
        ).get_payment_strategy()

        payment_context = PaymentStrategyContext(cash_payment_strategy)

        payment_context.make_payment(amount=100)

        payment_context.payment_strategy = paypal_payment_strategy
        payment_context.make_payment(amount=200)

        payment_context.payment_strategy = credit_card_payment_strategy
        payment_context.make_payment(amount=300)

        payment_context.payment_strategy = bank_transfer_payment_strategy
        payment_context.make_payment(amount=400)


if __name__ == "__main__":
    Main.run()
