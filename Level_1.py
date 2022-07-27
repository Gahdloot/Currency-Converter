print('Currency Converter using Just Functions and Dictionaries')

# Assign all the Values to their Variable
# Note the value added to this variables is Dated April 2nd 2022
ngn = 1
usd = 417
pounds = 547
euro = 460
clan = (usd, pounds, euro, ngn)


# input all the expected values as string into a list
Currencylist = ['usd', 'pounds', 'euro', 'ngn']


# request for first value
intial_currency = input('enter currency to convert From e.g (usd, pounds, euro, ngn) : ').lower()


# Open a dictionary where you can equate each list to input
conv = {
    'ngn': ngn,
    'usd': usd,
    'pounds': pounds,
    'euro': euro
}

# Conditionals to ensure input is from the list
while intial_currency not in Currencylist :
    print('invalid input !!!')
    intial_currency = input('enter currency to convert e.g (usd, pounds, euro, ngn) : ').lower()

# request for Second  value
values_to_convert_to = input('enter currency to convert to e.g (usd, pounds, euro, ngn) : ').lower()

# Conditionals to ensure input is from the list
while values_to_convert_to not in Currencylist :
    print('invalid input !!!')
    values_to_convert_to = input('enter currency to convert to e.g (usd, pounds, euro, ngn) : ').lower()

amount = int(input('enter figure to convert : '))


# function that converts the list
def converter(intial_currency, amount, values_to_convert_to):
    if type(intial_currency) is str:
        o = conv.get(intial_currency) * amount
        p = o / conv.get(values_to_convert_to)
        return p
    elif type(intial_currency) is int:
        o = intial_currency * amount
        p = o / values_to_convert_to
        return p


# run the Function.
converter(intial_currency, amount, values_to_convert_to)