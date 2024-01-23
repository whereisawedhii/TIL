# 아래 함수를 수정하시오.
def union_sets(a, b):
    result_set = a.union(b)

    return result_set


result = union_sets({1, 2, 3}, {3, 4, 5})
print(result)
