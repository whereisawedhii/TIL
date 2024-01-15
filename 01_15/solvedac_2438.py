# 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
num = int(input())

i = 0 
while i < num :
    i += 1
    print('*' * i)