# 아래 함수를 수정하시오.
def remove_duplicates(a):
    b = set(a)
    b = list(b)

    return b

result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(result)
