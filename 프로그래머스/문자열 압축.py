# 문자열 압축
# https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = []
    if len(s) == 1:
        return 1

    for j in range(1, (len(s)//2+1)):
        ans = []
        for i in range(0, (len(s)), j):
            ans.append(s[i:i+j])
            # 문자열 n개씩 자르기
    # ========================================
    # 같은 문자끼리 압축
        result = ans[0]  # ans 0번째 인덱스 값을 결과에 넣는다
        count = 0
        for st in ans:
            if st == result[-j:]:  # 같다면 count ++
                count += 1
            else:  # -------------------> 다르다면 result에 count와 st추가
                if count == 1:
                    result += st
                else:
                    result += str(count) + st
                    count = 1
        result += str(count)  # 마지막 count 넣기
        # 마지막 count가 1이 아닌 것만 넣기
        result = [result[:-1] if count == 1 else result]
        answer.append(len(result[0]))  # 문자열 길이를 answer에 저장

    return min(answer)  # answer의 가장 작은 값 리턴

###############################################################################
# 정규 표현식 사용
# 프로그래머스 대장답


def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer
