#6 Display Fibonacci numbers the number you choose or less

max_num = int(input("Input number:"))

a = 1
b = 1

print(1)

while b <= max_num:
    a, b = b, a + b
    print(a)