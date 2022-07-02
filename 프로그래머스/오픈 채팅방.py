# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(record):
    uid_name = {}
    ans = []
    # 반복을 돌며 문자를 공백분리 하여 ans에 저장
    for i in record:
        an = i.split()
        ans.append(an)
        # Enter or Change 했을 경우 uid의 최종값을 dic형식으로 저장
        if an[0] in ['Enter', 'Change']:
            uid_name[an[1]] = an[2]

    answer = []

    for i in range(len(ans)):
        if ans[i][0] == "Enter":
            answer.append('{}님이 들어왔습니다.'.format(uid_name[ans[i][1]]))
        elif ans[i][0] == "Leave":
            answer.append('{}님이 나갔습니다.'.format(uid_name[ans[i][1]]))
    return answer
