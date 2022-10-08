from sys import stdin

test_case_cnt = int(stdin.readline())

for _ in range(test_case_cnt):
    c, v = map(int, stdin.readline().split())

    brother_candies = c // v

    dad_candies = c - v * brother_candies

    print(f"you get {brother_candies} pices(s) and your dad gets {dad_candies} piece(s).")