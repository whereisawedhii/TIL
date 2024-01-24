import sys
sys.stdin = open('input.txt', 'r')

import sys

N = int(sys.stdin.readline())
max_list= [int(sys.stdin.readline()) for i in range(N)]

max_list.sort(reverse=True)
max_weight = 0
length = len(max_list) 

for i in range(len(max_list)) : 
    possible_weight = max_list[i] * (i+1)
    if possible_weight >= max_weight : 
        max_weight = possible_weight

print(max_weight)
