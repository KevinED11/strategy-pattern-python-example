import abc
import enum

class PaymentStrategy(abc.ABC):
    @abc.abstractmethod
    def pay(self, amount: int) -> None:
        pass


class CashPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paid {amount} with cash')


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paid {amount} with credit card')


class DebitCardPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paid {amount} with debit card')


class PayPalPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paid {amount} with PayPal')


class BankTransferPayment(PaymentStrategy):
    def pay(self, amount: int) -> None:
        print(f'Paid {amount} with bank transfer')


class PaymentContext:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.__payment_strategy = payment_strategy

    @property
    def payment_strategy(self) -> PaymentStrategy:
        return self.__payment_strategy

    @payment_strategy.setter
    def payment_strategy(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def make_payment(self, amount: int) -> None:
        self.payment_strategy.pay(amount)


class AvailablePaymentMethods(enum.StrEnum):
    CREDIT_CARD = 'credit_card'
    DEBIT_CARD = 'debit_card'
    PAYPAL = 'paypal'
    BANK_TRANSFER = 'bank_transfer'
    CASH = 'cash'


def Factory(payment_method: AvailablePaymentMethods) -> PaymentStrategy:
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
        credit_card_payment = Factory(AvailablePaymentMethods.CREDIT_CARD)
        paypal_payment = Factory(AvailablePaymentMethods.PAYPAL)
        cash_payment = Factory(AvailablePaymentMethods.CASH)

        payment_context = PaymentContext(cash_payment)


if __name__ == '__main__':
    Main.run()
