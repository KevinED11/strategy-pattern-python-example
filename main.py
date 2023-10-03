import abc
import enum


class PaymentStrategy(abc.ABC):
    @abc.abstractmethod
    def pay(self, amount: int) -> None:
        pass


class CashPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with cash")


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with credit card")


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with debit card")


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with PayPal")


class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f"Paid {amount} with bank transfer")


class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.__payment_strategy = payment_strategy

    def make_payment(self, amount: int) -> None:
        self.__payment_strategy.pay(amount)

    @property
    def payment_strategy(self) -> PaymentStrategy:
        return self.__payment_strategy

    @payment_strategy.setter
    def payment_strategy(self, payment_strategy: PaymentStrategy) -> None:
        self.__payment_strategy = payment_strategy


class AvailablePaymentMethods(enum.StrEnum):
    CREDIT_CARD = "credit_card"
    DEBIT_CARD = "debit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"
    CASH = "cash"


def factory(payment_method: AvailablePaymentMethods) -> PaymentStrategy:
    available_methods = {
        "credit_card": CreditCardPayment,
        "debit_card": DebitCardPayment,
        "paypal": PayPalPayment,
        "bank_transfer": BankTransferPayment,
        "cash": CashPayment,
    }

    return available_methods[payment_method]()


class Main:
    @staticmethod
    def run() -> None:
        credit_card_payment = factory(AvailablePaymentMethods.CREDIT_CARD)
        paypal_payment = factory(AvailablePaymentMethods.PAYPAL)
        cash_payment = factory(AvailablePaymentMethods.CASH)
        bank_transfer_payment = factory(AvailablePaymentMethods.BANK_TRANSFER)

        payment_context = PaymentContext(payment_strategy=cash_payment)

        payment_context.make_payment(100)

        payment_context.payment_strategy = paypal_payment
        payment_context.make_payment(200)

        payment_context.payment_strategy = credit_card_payment
        payment_context.make_payment(300)

        payment_context.payment_strategy = bank_transfer_payment
        payment_context.make_payment(400)


if __name__ == "__main__":
    Main.run()
