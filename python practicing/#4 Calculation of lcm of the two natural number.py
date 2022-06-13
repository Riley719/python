#4 Calculation of lcm of the two natural number
x, y = int(input("Input number 1:")), int(input("Input number 2:"))

product = x * y

if x < y:
    x, y = y, x

while y !=1:
    if x % y == 0:
        break
    y, x = x % y, y

print(product // y)