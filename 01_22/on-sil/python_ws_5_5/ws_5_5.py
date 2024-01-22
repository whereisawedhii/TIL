# 아래 함수를 수정하시오.

# first commit 
# def even_elements(a):
#     even_list = []


#     for each in a :
#         if each % 2 == 0 :
#             popped = a.pop(a.index(each))
#             even_list.extend([popped])

#     return even_list


# another solution
def even_elements(a):
    even_list = []


    for each in a :
        if each % 2 == 0 :
            popped = a.pop(a.index(each))
            even_list.extend([popped])

    return even_list


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
