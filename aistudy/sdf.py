#핵심 소스코드의 설명을 주석으로 작성하면 평가에 큰 도움이 됩니다.
def solution(n):
    first = 0;
    second = 1;
    third = 0;
    if n == 0:
        return 0
    if n == 1:
        return 1
    for i in range(n - 1):
        third = first + second
        first = second
        second = third
    return third

print(solution(2))