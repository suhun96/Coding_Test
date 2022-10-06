# 딕셔너리로 풀기
n = int(input())

for _ in range(n):
    p = int(input())
    dic = {}
    for _ in range(p):
        cost, Player = input().split()
        Cost = int(cost)
        dic[Cost] = Player

    print(dic.get(max(dic.keys())))

#
n = int(input())
for i in range(n):
    p = int(input)
    max = 0
    for i in range(p):
        c, name = input().split()
        c = int(c)
        if c > max:
            max = c
            mName = name
    print(mName)