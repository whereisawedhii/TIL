import sys
sys.stdin = open('input.txt', 'r')

import sys

N = int(sys.stdin.readline())
max_list = list(map(int, sys.stdin.readline().split()))
max_list.sort()

sum = 0
mini_sum = 0

for each in max_list :
    mini_sum += each 
    sum += mini_sum

print(sum)
