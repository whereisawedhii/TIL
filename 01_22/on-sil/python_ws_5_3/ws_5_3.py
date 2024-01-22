# 아래 함수를 수정하시오.
def sort_tuple(x):
    new_tuple = ()

    list1 = list(x)
    list1.sort()
    
    new_tuple = tuple(list1)

    return new_tuple

result = sort_tuple((5, 2, 8, 1, 3))
print(result)
