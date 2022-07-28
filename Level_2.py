class currency:
    # Assign all the Values to their Variable
    # Note the value added to this variables is Dated April 2nd 2022
    usd = 417
    pounds = 547
    euro = 460
    ngn = 1

    hh = [usd, pounds, euro, ngn]
    hw = ['ngn', 'usd', 'euro', 'pounds']

    def __init__(self, convert_from, convert_to):
        self.convert_from = convert_from
        self.convert_to = convert_to
        self.amount = None

        if self.convert_from not in currency.hw:
            print(f'there is no file with the value {self.convert_from}')
        if self.convert_to not in currency.hw:
            print(f'there is no file with the value {self.convert_to}')

    def __str__(self):
        return f'the currency  is a {self.convert_from} that is being converted to {self.convert_to}'

    def __del__(self):
        return f'you have deleted the object of converting \n {self.convert_from} to {self.convert_to}'

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
            return (conv.get(self.convert_from) * self.amount) / conv.get(self.convert_to)

        except TypeError:
            print('check currency spellings, one seems to be wrong')

        except NameError:
            print('figure should be a number')




# all others can be tried.
