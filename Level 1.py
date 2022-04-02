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
r = input('enter currency to convert From e.g (usd, pounds, euro, ngn) : ').lower()


# Open a dictionary where you can equate each list to input
conv = {
    'ngn': ngn,
    'usd': usd,
    'pounds': pounds,
    'euro': euro
}

# Conditionals to ensure input is from the list
while r not in Currencylist :
    print('invalid input !!!')
    r = input('enter currency to convert e.g (usd, pounds, euro, ngn) : ').lower()

# request for Second  value
cc = input('enter currency to convert to e.g (usd, pounds, euro, ngn) : ').lower()

# Conditionals to ensure input is from the list
while cc not in Currencylist :
    print('invalid input !!!')
    cc = input('enter currency to convert to e.g (usd, pounds, euro, ngn) : ').lower()

g = int(input('enter figure to convert : '))


# function that converts the list
def converter():
    o = conv.get(r) * g
    p = o / conv.get(cc)
    print(f'you have {p}{cc}')

# run the Function
converter()