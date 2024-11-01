class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    @property
    def amount(self):
        return self.__amount
    
    @amount.setter
    def amount(self, n):
        self.__amount = n

    @property
    def currency(self):
        return self.__currency
    
    @currency.setter
    def currency(self, string):
        self.__currency = string

    def __add__(self, other):
        if self.currency == other.currency:    
            return Money(
                self.amount + other.amount,
                self.currency
                )
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __sub__(self, other):
        if self.currency == other.currency:    
            return Money(
                self.amount - other.amount,
                self.currency
                )
        else:
            raise RuntimeError("Mismatched currencies!")
        
    def __mul__(self, number):
        return Money(self.amount*number, self.currency)