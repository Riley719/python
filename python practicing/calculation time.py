import time
import math


def calculation_time(n):
    cal_time = 0
    for j in range(100):

        start = time.perf_counter()

        prime = list(range(n + 1))

        i = 2
        while i < math.sqrt(n):
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

        end = time.perf_counter()

        cal_time += end - start

    return print(cal_time/100)


max_num = int(input("Input number:"))
calculation_time(max_num)