import sys
sys.stdin = open('input.txt', 'r')

import sys

numbers = [int(sys.stdin.readline().strip()) for i in range(9)]

biggest_num = max(numbers)

print(biggest_num)
print(numbers.index(biggest_num)+1)