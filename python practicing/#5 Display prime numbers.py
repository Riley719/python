#5-1 Display prime numbers the number you choose or less

import time



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