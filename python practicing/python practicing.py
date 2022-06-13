#python practicing


#1 Hello World
print("Hello World")


#2 The sum of natural numbers from 1 to 50

sum = 0
for i in range(50):
    sum += i + 1
print(sum)


#3 Calculation of gcd of the two natural number
x, y = int(input("Input number 1:")), int(input("Input number 2:"))

if x < y:
    x, y = y, x

while y !=1:
    if x % y == 0:
        break
    y, x = x % y, y

print(y)


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


#5 Display prime numbers the number you choose or less

max_num = int(input("Input number:"))

prime = [2]

p = 3
prime_judge = 1

while p <= max_num:
    i = 0
    while i < len(prime):
        if p % prime[i] == 0:
            prime_judge = 0
            p += 2
            break
        else:
            i += 1

    if prime_judge == 1:
        prime.append(p)
        p += 2
    else:
        prime_judge = 1

for i in range(len(prime)):
    print(prime[i])

#6 Display Fibonacci numbers the number you choose or less

max_num = int(input("Input number:"))

a = 1
b = 1

print(1)

while b <= max_num:
    a, b = b, a + b
    print(a)


#7 




