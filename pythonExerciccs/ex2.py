#factorial

def factorial(x):        
    if x < 0:
        return "factorial does not support negative numbers"
    elif x == 0:
        return 1
    else:
        return x*factorial(x-1)

try:
    x = int(input('saisie entier : '))
    print(factorial(x))
except:
    print('Entier svp')
