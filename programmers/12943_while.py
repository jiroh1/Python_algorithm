'''
콜라츠 추측
https://school.programmers.co.kr/learn/courses/30/lessons/12943
문제 설명
1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될 때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다. 작업은 다음과 같습니다.

1-1. 입력된 수가 짝수라면 2로 나눕니다.
1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.
예를 들어, 주어진 수가 6이라면 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 이 되어 총 8번 만에 1이 됩니다. 위 작업을 몇 번이나 반복해야 하는지 반환하는 함수, solution을 완성해 주세요. 단, 주어진 수가 1인 경우에는 0을, 작업을 500번 반복할 때까지 1이 되지 않는다면 –1을 반환해 주세요.

제한 사항
입력된 수, num은 1 이상 8,000,000 미만인 정수입니다.
입출력 예
n	result
6	8
16	4
626331	-1
입출력 예 설명
입출력 예 #1
문제의 설명과 같습니다.

입출력 예 #2
16 → 8 → 4 → 2 → 1 이 되어 총 4번 만에 1이 됩니다.

입출력 예 #3
626331은 500번을 시도해도 1이 되지 못하므로 -1을 리턴해야 합니다.

※ 공지 - 2022년 6월 10일 다음과 같이 지문이 일부 수정되었습니다.

주어진 수가 1인 경우에 대한 조건 추가
'''
# 연습과정
# answer = 0
# num = 6
# for i in range(5):
#     if num % 2 == 0:
#         num = num / 2
#         print(type(num),'!!!')
#         print(num,'num!')
#         answer += 1
#         if num % 2 == 0:
#             num = num/2
#             answer += 1
#         elif num % 2 == 1:
#             num = num * 3 + 1
#             answer += 1
#     print(answer,'ans')
'---------------------'
# num = 6
# answer = 0
# while num > 1 :
#     if num % 2 == 0:
#         num = num / 2
#         answer += 1
#     elif num % 2 == 1:
#         num = num * 3 + 1
#         answer += 1
#     elif answer > 499 :
#
# print(answer ,' !')
# # 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#답
def solution(num):
    answer = 0
    while num > 1: # while num !=: 이렇게 쓴 사람들이 많았음
        if num % 2 == 0:
            num = num / 2
            answer += 1
        elif num % 2 == 1:
            num = num * 3 + 1
            answer += 1
    if answer < 500:
        return answer
    else:
        return -1


print(solution(6))  # result : 8
print(solution(16))  # result : 4
print(solution(626331))

'''
정리 : 
    1. while 하나에서 모든 것을 끝내려고 해서 좀 오래 걸렸다.
    2. 반복문 진행 시 내가 생각한 방향으로 진행 되지 않아서 반복문 없이 한바퀴 도는 것으로 진행해서 문제가 풀림
    3. 500번 제한이 있으니깐 for 문으로 갔어도 가능 함 

다른 답 : 
case #1
def collatz(num):
    for i in range(501):
        if num == 1:
            return i
        num = num/2 if num%2==0 else num*3+1
    return -1
    
'''