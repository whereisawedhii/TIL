# import sys
# sys.stdin = open('input.txt', 'r')


# N, money = map(int, sys.stdin.readline().split())
# coins= [int(sys.stdin.readline().strip()) for i in range(N)]

# coins.sort(reverse=True)
# counts = 0

# for i in coins : 
#     if i < money : 
#         counts += money // i
#         money = money % i

# print(counts)


N, money = map(int, input().split())
coins= [int(input()) for i in range(N)]
coins.sort(reverse=True)
counts = 0

for i in coins : 
        counts += money // i
        money = money % i

print(counts)