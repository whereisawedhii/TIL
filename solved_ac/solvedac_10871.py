# 정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 
# 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.

# N, X = map(int, input().split())
# A = list(map(int, input().split()))
# result_list = []

# i=0 
# while i < N :
#     if A[i] < X :
#         result_list.append(A[i])
#         i += 1 
#     else : 
#         i += 1

# length_result = len(result_list)

# i=0
# while i < length_result :
#     print(f"{result_list[i]}"+" ")
#     i += 1
#     if i == length_result : 
#         break

N, X = map(int, input().split())
A = list(map(int, input().split()))
result_list = []

i = 0
while i < N:
    if A[i] < X:
        result_list.append(A[i])
    i += 1

for num in result_list:
    print(f"{num}", end=" ")
