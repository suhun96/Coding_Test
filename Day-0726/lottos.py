def solution1(lottos, win_nums):
    # 민우 로또번호 lottos, 당첨 번호 win_nus
    cnt_corr = 0
    cnt_zero = 0
    
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt_corr += 1
        if lottos[i] == 0:
            cnt_zero += 1 
            
    total = cnt_corr + cnt_zero
    
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6} 
    
    answer = [rank[total], rank[cnt_corr]]
    
    
    return answer

def solution2(lottos, win_nums):

    rank=[6,6,5,4,3,2,1] # 딕셔너리 쓰지않고 순서대로 당첨 내용 리스트로!

    cnt_0 = lottos.count(0) # 찾고자 하는 항목이 파이썬의 리스트에 몇개나 들어있는지 확인하는 count 함수
    cor = 0
    for x in win_nums:
        if x in lottos:
            cor += 1
    return rank[cnt_0 + cor],rank[cor]
