#fewest coins
price = int(input('enter item price (in pennies :'))

amount_owed = 100-price
#calculate coin amounts
#quarters
quarters = amount_owed // 25 
if quarters != 0:
    print(f'{quarters} quarters')
#dimes
amount_owed %= 25
dimes = amount_owed // 10
if dimes != 0:
    print(f'{dimes} dimes')
#nickles
amount_owed %= 5
nickles = amount_owed // 5
if nickles != 0:
    print(f'{nickles} nickles')
#pennies
pennies = amount_owed % 5
if pennies != 0:
    print(f'{pennies} pennies')