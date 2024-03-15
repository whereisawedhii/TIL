'''
테트리스의 모형은 총 19개
해당 모형들을 3가지 유형으로 나눔
1.      x1x
        x1x
        x1x
         x
    세로 3칸에서  x쳐진 영역들을 하나씩 더하면 7가지 모형 커버

2.      xxx
        111x
        xxx
    가로 3칸에서 x쳐진 영역들을 하나씩 더하면 7가지 모형 커버

3.      11  11   x11    1   1
        11  x11  11    11   11
                       1x   x1
    네모를 만들고, 해당 칸에서 1칸씩 빼고, 한칸씩 더하여 5가지 모형 커버
    x는 기존 네모에서 삭제된 칸을 뜻함

이렇게 a, b, c 3가지 유형으로 테트로미노를 만들어
최댓값에 반영하는 함수를 만들어서 nxm 순회하여 각각 진행함

'''

import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline


def tetris_a(i, j, sum_a):
    global max_v

    flag_a = 1
    for a in range(1, 3):
        if i + a >= N:
            flag_a = 0
            break
        else:
            sum_a += arr[i + a][j]
    if flag_a:
        a_max = 0
        for k in range(7):
            ni, nj = i+tet_a[k][0], j+tet_a[k][1]
            if 0 <= ni < N and 0 <= nj < M:
                if a_max < arr[ni][nj]:
                    a_max = arr[ni][nj]
        if max_v < sum_a + a_max:
            max_v = sum_a + a_max
    else:
        return


def tetris_b(i, j, sum_b):
    global max_v

    flag_b = 1
    for b in range(1, 3):
        if j + b >= M:
            flag_b = 0
            break
        else:
            sum_b += arr[i][j + b]
    if flag_b:
        b_max = 0
        for k in range(7):
            ni, nj = i + tet_b[k][0], j + tet_b[k][1]
            if 0 <= ni < N and 0 <= nj < M:
                if b_max < arr[ni][nj]:
                    b_max = arr[ni][nj]
        if max_v < sum_b + b_max:
            max_v = sum_b + b_max
        return
    else:
        return


def tetris_c(i, j, sum_c):
    global max_v

    flag_c = 1
    for c in range(3):
        ni, nj = i+make_c[c][0], j+make_c[c][1]
        if ni < N and nj < M:
            sum_c += arr[ni][nj]
        else:
            flag_c = 0
            break
    if flag_c:
        c_max = 0
        for k in range(4):
            mi, mj = i+tet_c[k][0][0], j+tet_c[k][0][1]
            ni, nj = i + tet_c[k][1][0], j + tet_c[k][1][1]
            if 0 <= ni < N and 0 <= nj < M:
                if c_max < arr[ni][nj]-arr[mi][mj]:
                    c_max = arr[ni][nj]-arr[mi][mj]
        if max_v < sum_c + c_max:
            max_v = sum_c + c_max
        return
    else:
        return


make_c = ((1, 0), (0, 1), (1, 1))
tet_a = ((0, 1), (0, -1), (1, 1), (1, -1), (2, 1), (2, -1), (3, 0))
tet_b = ((-1, 0), (1, 0), (-1, 1), (1, 1), (-1, 2), (1, 2), (0, 3))
tet_c = (((1, 1), (-1, 1)), ((1, 0), (-1, 0)), ((1, 0), (1, 2)), ((0, 0), (0, 2)))

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
max_v = 0

for i in range(N):
    for j in range(M):
        # start 지점을 정함
        start = arr[i][j]
        a = tetris_a(i, j, start)
        b = tetris_b(i, j, start)
        c = tetris_c(i, j, start)

print(max_v)
