'''
python -m venv venv
크기가 N×N인 도시
도시에 있는 치킨집 중에서 최대 M개를 고르고,
나머지 치킨집은 모두 폐업시켜야 한다.

도시의 칸은 (r, c)와 같은 형태로 나타내고,
r행 c열
또는 위에서부터 r번째 칸,
왼쪽에서부터 c번째 칸을 의미한다.
r과 c는 1부터 시작한다.

입력
N(2 ≤ N ≤ 50)과 M(1 ≤ M ≤ 13)
둘째 줄부터 N개의 줄에는 도시의 정보
치킨집의 개수는
M보다 크거나 같고, 13보다 작거나 같다

출력
폐업시키지 않을 치킨집을 최대 M개를 골랐을 때,
도시의 치킨 거리의 최솟값을 출력

input 값 받을 때
2 -> 치킨
1 -> 인간
으로 각각 따로 저장하면서 받는다
인간을 순회하면서
치킨집을 순회함
min_v =
치킨집x - 인간x + 치킨집y - 인간y
중 가장 짧은 거리를 구함

'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from itertools import combinations

N, M = map(int, input().split())

arr = []
chickens = []
houses = []
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        if tmp[j]:
            if tmp[j] == 2:
                chickens.append((i, j))
            elif tmp[j] == 1:
                houses.append((i, j))

for bbqs in combinations(chickens, M):
    for bbq in bbqs:

        bbq[0]