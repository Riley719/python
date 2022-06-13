#5-3 Display prime numbers the number you choose or less
#In terms of Euler method

def gcd(a, b):
    if a < b:
        a, b = b, a


    if b == 1:
        return 1

    elif a == 0:
        return 0

    elif b % a == 0:
        return 0

    elif a & 1 == 1 and b & 1 == 0:
        return gcd(a - b, b // 2)
    
    elif a & 1 == 1 and b & 1 == 1:
        return gcd((a - b) // 2, b)


print(2)

print(gcd(99, 36))