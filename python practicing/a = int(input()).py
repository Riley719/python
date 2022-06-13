R, C = map(int, input().split())
A_11, A_12 = map(int, input().split())
A_21, A_22 = map(int, input().split())

if R == 1 and C == 1:
    print(A_11)

elif R == 1 and C == 2:
    print(A_12)

elif R == 2 and C == 1:
    print(A_21)

elif R == 2 and C == 2:
    print(A_22) 