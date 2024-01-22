# 아래 함수를 수정하시오.
def find_min_max(a):
    a.sort()
    min_num = a[0]
    a.sort(reverse=True)
    max_num = a[0]
    return (min_num, max_num)

# # 보충 - without method
# def find_min_max(a):
#     min_num = a[0]
#     max_num = a[0]
#     for i in a : 
#         if min_num > i :
#             min_num = i
#         elif max_num < i :
#             max_num = i
#     return (min_num, max_num)

result = find_min_max([3, 1, 7, 2, 5])
print(result)  # (1, 7)
