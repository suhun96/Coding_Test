def solution(board, moves):
    answer = 0
    bucket = [] # 인형을 담음

    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0: # 0이 안니면 인형을 뽑아서 bucket으로 옮김
                bucket.append(board[i][move-1])
                board[i][move-1] = 0 # 뽑힌 인형자리를 바꿈
            
                if len(bucket) > 1:
                    if bucket[-1] == bucket[-2]:
                        bucket.pop()
                        bucket.pop()
                        answer += 2
                break # 인형을 꺼냈는데 또 아래로 내려갈 수 있음. move 한번에 한 인형만 뽑히도록 멈춤
    return answer