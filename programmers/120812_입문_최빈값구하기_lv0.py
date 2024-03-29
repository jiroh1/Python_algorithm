"""
최빈값 구하기
https://school.programmers.co.kr/learn/courses/30/lessons/120812
"""
from collections import Counter

def solution(numbers):
    c = Counter(numbers).most_common()
    c_list=[c[i][1] for i in range(len(c))]
    c_list=sorted(c_list, reverse= True)
    if c_list.count(c_list[0]) > 1:
        return -1
    else:
        return c[0][0]
# 최빈 값 return
# 최빈 값이 여러개면 -1
numbers = [1, 2, 3, 3, 3, 4]
# numbers = [1, 1, 2, 2]
print(solution(numbers))

"""
문제
최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다. 
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요. 
최빈값이 여러 개면 -1을 return 합니다.

제한사항
0 < array의 길이 < 100
0 ≤ array의 원소 < 1000
입출력 예
array	result
[1, 2, 3, 3, 3, 4]	3
[1, 1, 2, 2]	-1
[1]	1
입출력 예 설명
입출력 예 #1

[1, 2, 3, 3, 3, 4]에서 1은 1개 2는 1개 3은 3개 4는 1개로 최빈값은 3입니다.
입출력 예 #2

[1, 1, 2, 2]에서 1은 2개 2는 2개로 최빈값이 1, 2입니다. 최빈값이 여러 개이므로 -1을 return 합니다.
입출력 예 #3

[1]에는 1만 있으므로 최빈값은 1입니다.
"""
"""
정리
1. counter 함수에 대해서 알았으면 되는 문제
2. 그 후 집중 안하고 다른 답만 찾아 보려고 했던 듯.
3. 풀이도 많이 없고 이해가 안되서 그냥 없다고 생각하고, 문제 그대로 풀이하니 오히려 잘 풀림
"""
"""
다른풀이
# case1
def solution(array):
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1

"""
"""
참고
list 안에 위치 찾기
https://eggwhite0.tistory.com/75
counter
https://codepractice.tistory.com/71
"""