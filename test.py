import unittest
from wallet import Wallet


class WalletUnitTest(unittest.TestCase):

    def setUp(self):
        self.wallet = Wallet()

    def test_show_balance(self):
        self.wallet.add_data('income', 200, 'Test income')
        self.wallet.add_data('expense', 50, 'Test expense')

        income = sum(data['Miqdor'] for data in self.wallet.informations if data['Turkum'] == 'income')
        expenses = sum(data['Miqdor'] for data in self.wallet.informations if data['Turkum'] == 'expense')

        self.assertEqual(income - expenses, 150)

    def test_add_data(self):
        initial_count = len(self.wallet.informations)

        # add income data
        self.wallet.add_data("income", 221, "Profit from trading")
        self.assertEqual(len(self.wallet.informations), initial_count + 1)

        # add expense data
        self.wallet.add_data("expense", 185, "Paid for advanced course")
        self.assertEqual(len(self.wallet.informations), initial_count + 2)

    def test_edit_data(self):
        # add initial data for edit
        self.wallet.add_data("income", 221, "Profit from trading")

        # edit data
        edit_index = 0
        new_data = {'Tavsif': "something changed"}
        self.wallet.edit_data(edit_index, new_data)

        self.assertEqual(self.wallet.informations[edit_index]['Tavsif'], "something changed")


if __name__ == '__main__':
    unittest.main()
