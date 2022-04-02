class currency:
    # Assign all the Values to their Variable
    # Note the value added to this variables is Dated April 2nd 2022
    usd = 417
    pounds = 547
    euro = 460
    ngn = 1

    hh = [usd, pounds, euro, ngn]
    hw = ['ngn', 'usd', 'euro', 'pounds']

    def __init__(self, confro, conto):
        self.confro = confro
        self.conto = conto
        self.amount = None

        if self.confro not in currency.hw:
            print(f'there is no file with the value {self.confro}')
        if self.conto not in currency.hw:
            print(f'there is no file with the value {self.conto}')

    def __str__(self):
        return f'the currency  is a {self.confro} that is being converted to {self.conto}'

    def __del__(self):
        return f'you have deleted the object of converting \n {self.confro} to {self.conto}'

    def convert(self, amount=1):
        self.amount = amount

        conv = {
            'ngn': currency.ngn,
            'usd': currency.usd,
            'pounds': currency.pounds,
            'euro': currency.euro
        }

        if type(self.amount) != int:
            raise NameError('Type is wrong')


        try:
            print(f'{self.amount}{self.confro} is equals to {(conv.get(self.confro) * self.amount) / conv.get(self.conto)}{self.conto}')

        except TypeError:
            print('check currency spellings, one seems to be wrong')

        except NameError:
            print('figure should be a number')


usdngn = currency('usd', 'ngn')

print(usdngn)
usdngn.convert()

# all others can be tried.
