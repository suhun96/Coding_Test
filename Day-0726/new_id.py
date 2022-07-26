def solution(new_id):
    answer = ''
    
    #step1
    new_id = new_id.lower()
    
    #step2
    for id in new_id:
        if id.isalnum() or id in ['-', '_', '.']:
            answer += id
            
    #step3
    while '..' in answer:
        answer = answer.replace('..', '.')
    
    #step4
    if answer[0] == '.' and len(answer) > 1:
        answer = answer[1:]
    if answer[-1] == '.':
        answer = answer[:-1]
    
    #step5
    if answer =='':
        answer = 'a'
    
    #step6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    
    #step7
    while len(answer) < 3:
        answer += answer[-1]
        
    
        
    return answer

    