class CreditCard:
    """A Consumer CreditCard"""

    def __init__(self, customer, bank, account, limit):
        """ Creates a new CreditCard instance
        The initial balance is 0

        customer    the name of the customer \n
        bank        the name of the bank \n
        account     the account identifier \n
        limit       credit limit \n
        """

        self._customer = customer
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return the bank's name"""
        return self._bank

    def get_accout(self):
        """Return the card identifying number (Typically stored as String)"""
        return self._account

    def get_limit(self):
        """Return the current Credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """Charge given price to the Card, assuming sufficient credit limit

        Return True if charge was processed, False if charge was denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payemnt(self, amount):
        """Process Customer payment that reeduces balance"""
        self._balance -= amount


if __name__ == "__main__":
    wallet = [(CreditCard('John Bowman', 'California Savings',
                          '56 5391 0375 9387 5309', 2500)), (CreditCard('John Bowman', 'California Federal',
                                                                        '58 3485 0399 3395 1954', 3500)),
              (CreditCard('John Bowman', 'California Finance',
                          '60 5391 0375 9387 5309', 5000))]

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2 * val)
        wallet[2].charge(3 * val)

    for c in range(3):
        print(f'Customer: {wallet[c].get_customer()}')
        print(f'Bank:  {wallet[c].get_bank()}')
        print(f'Account: {wallet[c].get_accout()}')
        print(f'Limit: {wallet[c].get_limit()}')
        print(f'Balance: {wallet[c].get_balance()}')
        while wallet[c].get_balance() > 100:
            wallet[c].make_payemnt(100)
            print(f'New Balance: {wallet[c].get_balance()}')
        print()


class PredatoryCreditCard(CreditCard):
    """An extension to credit card that compound interest and fees"""

    def __init__(self, customer, bank, account, limit, apr):
        """Create a new predatory CreditCard instance 

        The initail balance is zero

        customer    the name of the customer \n
        bank        the name of the bank \n
        account     the account identifier \n
        limit       credit limit \n
        apr         annual percentage rate (0.0825 for 8.25% APR) """

        super().__init__(customer, bank, account, limit)
        self._apr = apr

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit

        Return True if charge was processed.
        Return False and asses $5 fee if charge is denied
        """

        success = super().charge(price)
        if not success:
            self._balance += 5

        return success

    def process_month(self):
        """Asses monthly interest on outstanding balance"""

        if self._balance > 0:
            self._balance += (((self._apr / 12) / 100) * self._balance)
