import sys
sys.stdin = open('input.txt', 'r')

import sys
T = int(sys.stdin.readline())


for i in range(T) : 
    H, W, N = map(int, sys.stdin.readline().split())
    floor = N % H 
    walk = N // H + 1 
    
    if N % H == 0 :
        floor = H 
        walk = N // H

    if walk < 10 : 
        walk = '0'+str(walk)

    print(str(floor)+str(walk))