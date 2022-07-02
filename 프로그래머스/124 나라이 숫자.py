# https://programmers.co.kr/learn/courses/30/lessons/12899?language=python3

def solution(n):
    answer = []

    while n:
        n, b = divmod(n, 3)  # 3으로 나눈 몫과 나머지
        if b == 0:  # 나머지가 0이면
            n -= 1
            answer.append(4)
        else:
            answer.append(b)
    ans = list(reversed(answer))

    return ["".join([str(i) for i in ans])][0]
