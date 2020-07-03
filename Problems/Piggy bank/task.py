class PiggyBank:
    MAX_CENTS = 100

    def __init__(self, dollars, cents):
        self.dollars = dollars
        self.cents = cents

    def add_money(self, deposit_dollars, deposit_cents):
        dollars = (self.cents + deposit_cents) // self.MAX_CENTS
        cents = (self.cents + deposit_cents) % self.MAX_CENTS
        self.dollars += deposit_dollars + dollars
        self.cents = cents


