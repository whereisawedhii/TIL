'''
톱니바퀴 4개 : 1,2,3,4 번 
톱니 8개 : 12시 방향부터 주어짐 

01234567 일 때, 
맞물린 톱니 : 6번/2번, 6번/2번, 6번/2번 

톱니는 0, 1로 주어지고 
서로 같으면 회전하지 않고, 
다르면 반대방향으로 회전함 

시계방향 회전 : popleft -> append
반시계방향 회전 : pop -> appendleft

입력
초기 톱니바퀴 상태
회전 수 K
톱니바퀴 번호, 방향 (-1 반시계 1 시계)

출력
회전 이후 네 톱니바퀴 점수의 합 
1번 톱니바퀴 12시방향이 0이면 0점, 1이면 1점 
2번 톱니바퀴 12시방향이 0이면 0점, 1이면 2점 
3번 톱니바퀴 12시방향이 0이면 0점, 1이면 4점 
4번 톱니바퀴 12시방향이 0이면 0점, 1이면 8점 
'''
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
from collections import deque

def rotation(idx, dir):
    flag = [0]*4
    visited = [0]*4
    flag[idx] = dir
    visited[idx] = 1

    for _ in range(4):
        if not flag[idx]:
            continue
        else:
            if idx == 0:
                if arr[0][6] != arr[1][2]:
                    if not visited[1]:
                        visited[1] = 1
                        flag[1] = -dir
            elif idx == 1:
                if arr[1][2] != arr[0][6]:
                    if not visited[0]:
                        visited[0] = 1
                        flag[0] = -dir
                if arr[1][6] != arr[2][2]:
                    if not visited[2]:
                        visited[2] = 1
                        flag[2] = -dir
            elif idx == 2:
                if arr[2][2] != arr[1][6]:
                    if not visited[1]:
                        visited[1] = 1
                        flag[1] = -dir
                if arr[2][6] != arr[3][2]:
                    if not visited[3]:
                        visited[3] = 1
                        flag[3] = -dir
            elif idx == 3:
                if arr[3][2] != arr[2][6]:
                    if not visited[2]:
                        visited[2] = 1
                        flag[2] = -dir       
        idx = (idx+1) % 4

    for i in range(4):
        result = 0
        if flag[i]:
            if flag[i] == 1:
                num = arr[i].pop()
                arr[i].appendleft(num)       
            elif flag[i] == -1:
                num = arr[i].popleft()
                arr[i].append(num)
        result += arr[i][0]*2**(i-1)
    
    return result


arr = []
for _ in range(4):
    tmp = deque(map(int, input().strip()))
    arr.append(tmp)

print(*arr, sep='\n')
K = int(input())
for _ in range(K):
    idx, dir = map(int, input().split())
    print(idx, dir)
    result = rotation(idx-1, dir)
    print(*arr, sep='\n')

print(result)