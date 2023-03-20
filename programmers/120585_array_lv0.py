"""
머쓱이보다 키 큰 사람
https://school.programmers.co.kr/learn/courses/30/lessons/120585
"""
def solution(array, height):
    array=sorted(array,reverse=True)
    for i,compare in enumerate(array):
        print(i,compare,height)
        if compare<=height:
            return i
        elif array[-1] >height :
            return len(array)
    return 0



# array=[180,120,140]
array=[149,180,192,170]

print(solution(array,148))

"""
정리 
compare<=height 에서 '='을 안넣어서 통과가 안되었었음.
그 외에는 다 비슷했고, 다른 풀이로 하는것이 좋은 것 같다.
""" 
"""
문제 설명
머쓱이는 학교에서 키 순으로 줄을 설 때 몇 번째로 서야 하는지 궁금해졌습니다. 머쓱이네 반 친구들의 키가 담긴 정수 배열 array와 머쓱이의 키 height가 매개변수로 주어질 때, 머쓱이보다 키 큰 사람 수를 return 하도록 solution 함수를 완성해보세요.

제한사항
1 ≤ array의 길이 ≤ 100
1 ≤ height ≤ 200
1 ≤ array의 원소 ≤ 200
입출력 예
array	height	result
[149, 180, 192, 170]	167	3
[180, 120, 140]	190	0
입출력 예 설명
입출력 예 #1

149, 180, 192, 170 중 머쓱이보다 키가 큰 사람은 180, 192, 170으로 세 명입니다.
입출력 예 #2

180, 120, 140 중 190보다 큰 수는 없으므로 0명입니다.
"""

"""
다른풀이
# case1) 이게 가장 이상적인듯
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)
"""