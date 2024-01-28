# import sys
# sys.stdin = open('input.txt', 'r')

import sys

N, M, K = map(int, sys.stdin.readline().split())

if N % 2 == 1:
    N -= 1
    K -= 1

girls = N // 2
boys = M 

if girls > boys : 
    while girls != boys and K > 0 :
        girls -= 1
        K -= 2
        if K == 1 :
            K = 0
            print(boys)
            exit()

if girls < boys :
    while girls != boys and K != 0 : 
        boys -= 1
        K -= 1
        if K == 0 :
            print(girls)
            exit()

rest_num = K // 3
final_count = K % 3

if final_count == 2 :
    result = girls - rest_num -1
    print(result)
else : 
    result = girls - rest_num
    print(result)

