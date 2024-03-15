'''
축구를 하기 위해 모인 사람 N
N은 짝수
N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눈다.
Sij는 i와 j가 같은 팀에 속했을 때, 팀에 더해지는 능력치
팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합임
Sij는 Sji와 다를 수 있으며, Sij, Sji 모두 팀에 더해짐

스타트 팀과 링크 팀의 능력치의 차이의 최솟값

조합으로 부분집합 생성하는데 -> 스타트팀 생성
조합이 만들어지는 수 // 2
만큼만 해야 중복 안됨

만들었으면 set - 로 빼서 차집합 생성 -> 링크팀 생성

i : 0 -> N-1까지 순회
j는 i+1 -> N까지 순회
여기서 N은 팀원 수 (N//2)
순회하면서 각각 Sij Sji A값 B값에 더하고
차이 구하기
'''

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

1234 1234

개수 : N C N//2

