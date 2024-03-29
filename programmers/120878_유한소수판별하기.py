"""
유한소수 판별하기
https://school.programmers.co.kr/learn/courses/30/lessons/120878
"""

import fractions
def factorization(x):
    d = 2
    check=[]
    while d <= x:
        if x % d == 0:
            check.append(d)
            x = x / d

        else:
            d = d + 1
    return check
            
def solution(a, b):
    f=fractions.Fraction(a,b)
    div_f=factorization(f.denominator)
    if [2,5] == list(set(div_f)):
        return 1
    elif [2] ==list(set(div_f)):
        return 1
    elif [5] ==list(set(div_f)):
        return 1
    elif [] ==list(set(div_f)):
        return 1
    else:
        return 2

"""
다른풀이
# case 1
from math import gcd

def solution(a, b):
    b = b / gcd(a, b)
    for i in [2, 5]:
        while not b % i:
            b //= i

    return 1 if b == 1 else 2
"""
"""
정리
1. fractions으로 확인 후 소인수 분해 로 했는데, 안됨 . 68 에서  조건으로 95.8 까지 올림. div_f에 뭐가 있는지가 중요햇음.
2. 수학적인 문제라서 풀어보고 안되서 바로 풀이 찾으려고 했으나..?
3. 문제 조건인 " 기약분수로 나타내었을 때, 분모의 소인수가 2와 5만 존재해야 합니다." 이걸 보고 다시 시도 해서 조건을 다시 진행
4. 반례에 대해서 힌트를 찾아서 성공시킴
    반례 : 3500, 500    
    기대값 : 1
    리턴값 : 2
    정수도 유한소수이기 때문에 분자가 분모로 나누어 떨어지는 경우 유한소수이므로 1을 리턴해야 합니다.
5. 다른 풀이에서 최대공약수를 이용한 것을 봤는데, 최대공약수에 대해서 이번에 정리 하기 위해서 기입

"""

"""
참고
fractions
https://steemit.com/kr/@coinchuu/python
소인수분해
https://needneo.tistory.com/112
최대공약수
https://computer-science-student.tistory.com/584
"""