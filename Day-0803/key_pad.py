def solution(numbers, hand):
    answer = ''
    l_pos = [1,4,7]
    r_pos = [3,6,9]
    start_hand = ['*', '#'] # 시작하는 손의 위치 왼 지는 별, 오른속 엄지는 우물점자.
    
    # 키패드를 좌표로 나타내고 시작.
    key_pad = {
        1: (0,0), 2: (1,0), 3: (2,0),
        4: (0,1), 5: (1,1), 6: (2,1),
        7: (0,2), 8: (1,2), 9: (2,2),
        '*': (0,3), 0: (1,3), '#': (2,3)
    }
    
    for num in numbers:
        if num in l_pos:
            start_hand[0] = num
            answer += 'L'
        elif num in r_pos:
            start_hand[1] = num
            answer += 'R'
        # 2,5,8,0 의 누르기전에 어느 손이 가까운지 알아야한다.    
        else:
            near_hand = get_near_hand(key_pad, start_hand[0], start_hand[1], num, hand)
            if near_hand == 'L':
                answer += 'L'
                start_hand[0] = num
            else:
                answer += 'R'
                start_hand[1] = num
            
        
    return answer

def get_near_hand(key_pad, l, r, num, hand):
    left_dis = abs(key_pad[l][0] - key_pad[num][0]) + abs(key_pad[l][1] - key_pad[num][1])
    right_dis = abs(key_pad[r][0] - key_pad[num][0]) + abs(key_pad[r][1] - key_pad[num][1])
    
    if left_dis == right_dis:
        near_hand = 'L' if hand == 'left' else 'R'
    else:
        near_hand = 'L' if left_dis < right_dis else 'R'
    
    return near_hand