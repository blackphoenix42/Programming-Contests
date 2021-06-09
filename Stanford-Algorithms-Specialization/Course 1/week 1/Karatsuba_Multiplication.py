import math


def karatsuba(x, y):
    xStr = str(x)
    yStr = str(y)

    n = max(len(xStr), len(yStr))

    if n == 1:
        return x*y

    middle = math.ceil((float(n)/2))

    if n > len(xStr):
        a = 0
        b = x
    else:
        a = int(xStr[0:middle])
        b = int(xStr[middle:])

    if n > len(yStr):
        c = 0
        d = y
    else:
        c = int(yStr[0:middle])
        d = int(yStr[middle:])

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    gauss_trick = karatsuba(a+b, c+d)

    gauss_trick = gauss_trick - ac - bd

    pow = n/2
    pow = pow * 2

    return ac*(10**pow) + gauss_trick*(10**(pow / 2)) + bd


num1 = 3141592653589793238462643383279502884197169399375105820974944592
num2 = 2718281828459045235360287471352662497757247093699959574966967627

print(karatsuba(55, 24))

# 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
