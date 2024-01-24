import sys
sys.stdin = open('input.txt', 'r')


M = int(sys.stdin.readline())

long_pipes = list(map(int, sys.stdin.readline().split()))

N = int(sys.stdin.readline())

short_pipes = list(map(int, sys.stdin.readline().split()))

print(M, long_pipes, N, short_pipes, sep='\n')
