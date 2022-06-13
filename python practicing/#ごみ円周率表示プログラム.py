#ごみ円周率表示プログラム

import math

def basel(n):
    basel_number = 0
    for i in range(1, n + 1):
        basel_number += 1 / i ** 2
    return basel_number

max_num = int(input("正の整数を入れろ！："))

Pi = basel(max_num)
Pi = math.sqrt(Pi * 6)

print(Pi)

