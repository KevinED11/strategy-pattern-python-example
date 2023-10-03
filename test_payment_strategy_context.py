import unittest
from main import read_payment, AvailablePaymentStrategyMethods


class TestPaymentStrategyContext(unittest.TestCase):
    def setUp(self) -> None:
        self.context = read_payment(
            AvailablePaymentStrategyMethods.CREDIT_CARD
        ).get_payment_strategy()

    def test_credit_card_payment_strategy(self) -> None:
        ...

    def test_paypal_payment_strategy(self) -> None:
        ...

    def test_cash_payment_strategy(self) -> None:
        ...

    def test_bank_transfer_payment_strategy(self) -> None:
        ...


if __name__ == "__main__":
    unittest.main()
