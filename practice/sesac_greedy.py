"""
예제 : 거스름돈 문제
- 당신은 음식점의 계산을 도와주는 점원이다. 카운터에는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다.
손님에게 거슬러 줘야 할 돈이 N원일 때 거슬러 줘야할 동전의 최소 개수를 구하라. (단, N은 항상 10의 배수)
- 전체문제를 부분문제의 식으로 표현해볼 것
"""

# 거슬러 줘야할 돈 N -> 10의 배수
# 동전의 최소 개수
# N = 500 * a + 100 * b + 50 * c + 10 * d
"""
부분문제의 식으로 하고 이 문제에서는 순서가 중요하다. 
"""
n = 1150
answer = 0
while True:
    if n // 500 > 0:
        answer += n // 500
        # print(answer)
        n = (n % 500)
        if n == 0: break
    elif n // 100 > 0:
        answer += n // 100
        n = n % 100
        if n == 0: break
    elif n // 50:
        answer += n // 50
        n = n % 50
        if n == 0: break
    elif n // 10:
        answer += n // 10
        break


print('!!!', answer)

# 강사님 답안

money_list = [3530,
8710,
9900,
900,
450,
3930,
5780,
6730,
8290,
7300,
2830,
580,
6840,
920]

def solution2(N:int):
    answer = 0
    coins = [500, 100, 50, 10]
    for coin in coins:
        answer += N // coin
        N %= coin
    return answer

answer_list = []
for m in money_list:
    answer_list.append(solution2(m))

