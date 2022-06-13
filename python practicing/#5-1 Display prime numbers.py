#5 Display prime numbers the number you choose or less
#In terms of Euclid method

import time



max_num = int(input("Input number:"))

start = time.perf_counter()

print(2)

prime = [2]
p = 3

while p <= max_num:
    for i in prime:
        if p % i == 0:
            break

    else:
        prime.append(p)
        print(p)

    p += 2

end = time.perf_counter()

print("Calculation time:" + str(end - start))