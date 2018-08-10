import Module1
Amount=eval(input("Enter amount to be transferred:"))
if 0<Amount<=10000:
    print("Fund transfer successful")
elif Amount>=10000:
    raise Module1.InsufficientFunds("Amount entered is greaterthan limit")

if Amount==0:
    raise Module1.YouCantDivbyZero("You Can/'t!!!!!!!")
else:
    print(500000/Amount)
try:
    print('try')
    print(10/Amount)
except ZeroDivisionError:
    print('except')
    raise Module1.YouCantDivbyZero("You Can/'t!!!!!!!")
else:
    print('else')
finally:
    print('Finally')
