#初期値入力＆数値型に変換
collatz_number = int(input("初期値を入力してください："))
#計算回数
n = 2

#初期値を表示
print("1：" + str(collatz_number))

#コラッツ数の計算
while collatz_number != 1:
    #2の倍数のときは半分にし、その値を表示
    if collatz_number % 2 == 0:
        collatz_number = collatz_number // 2
        print(str(n) + "：" + str(collatz_number))
        n += 1
    #2の倍数でないときは3倍して1を足し、その値を表示
    else:
        collatz_number = 3 * collatz_number + 1
        print(str(n) + "：" + str(collatz_number))
        n += 1