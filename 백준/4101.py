import sys
input = sys.stdin.readline

while True :
    a, b = map(int, input().split())

    # 0 0 입력받으면 종료
    if a == 0 and b == 0 : break

    if a > b : print("yes")
    else : print("No")