id_list    = ["muzi", "frodo", "apeach", "neo"]
report     = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k          = 2

from collections import defaultdict


def solution1(id_list, report, k):
    id_list    = ["muzi", "frodo", "apeach", "neo"]
    report     = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    k = 2

    answer = []
    # 중복 신고 제거
    report = list(set(report))
    # user별 신고한 id 저장
    user = defaultdict(set)
    # 신고자가 신고한 id 추가
    cnt  = defaultdict(int)

    for r in report:
        # report의 첫번째 값은 신고자id, 두번째 값은 신고당한 id
        a,b = r.split()
        # 신고자가 신고한 id 추가
        user[a].add(b)
        # 신고당한 id의 신고 횟수 추가
        cnt[b] += 1

    for i in id_list:
        result = 0

        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    return answer


def solution2(id_list, report, k):
    answer = [0] * len(id_list)
    print(answer)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1
    print(reports)

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

solution2(id_list, report, k)