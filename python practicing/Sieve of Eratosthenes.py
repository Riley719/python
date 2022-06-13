#5-2 Display prime numbers the number you choose or less
#In terms of Eratosthenes method

import math

max_num = int(input("Input number:"))

prime = list(range(max_num + 1))


i = 2

while i <= math.sqrt(max_num):
    k = 2
    while i * k < len(prime):
        prime[i * k] = 0
        k += 1
    if i == 2:
        i += 1
    else:
        i += 2
    
for i in prime:
    if i == 0 or i == 1:
        continue
    else:
        print(i)