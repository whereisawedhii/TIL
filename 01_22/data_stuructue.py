# print(type('1')) # <class 'str'>
# print(type([1, 2])) # <class 'list'>

# # __###__ : 매직메서드 - 특수한 상황에서 자동으로 호출됨.. 
# print(help(list))
# |  append(self, object, /)
# |      Append object to the end of the list.
# 클래스 list 안에 내부적으로 정의되어 있는 함수


# my_str = 'banana'

# # find
# print(my_str.find('a')) # 1 - 첫 번째 index
# print(my_str.find('z')) # -1 

# # index
# print(my_str.index('a')) # 1
# print(my_str.index('z')) # ValueError

# isalpha
# string1 = 'Hello'
# string2 = '123'
# print(string1.isalpha()) #True
# print(string2.isalpha()) #False 

# str.replace(old, new[,count]) 

# my_list = [1, 2, 3]

# # append 
# my_list.append([4, 5, 6])
# print(my_list) # [1, 2, 3, [4, 5, 6]]
# print(my_list.append([4, 5, 6])) # None

# # extend
# my_list = [1, 2, 3]
# my_list.extend([4, 5, 6])
# print(my_list) # [1, 2, 3, 4, 5, 6]

# # index
# my_list = [1, 2, 3, 4, 5, 6]
# my_list.insert (3, 'ssafy')
# print(my_list) # [1, 2, 3, 'ssafy', 4, 5, 6]

# # remove
# my_list = [1, 2, 3, 'ssafy', 4, 4, 5, 6]
# my_list.remove(4)
# print(my_list) # [1, 2, 3, 'ssafy', 4, 5, 6]

# # pop - 리턴이 있음
# my_list = [1, 2, 3, 'ssafy', 4, 5, 6]
# item1 = my_list.pop()
# print(item1) # 6 
# item2 = my_list.pop(0)
# print(item2) # 1
# print(my_list) # [2, 3, 'ssafy', 4, 5]

# # clear 
# my_list.clear()
# print(my_list) # []

# # index 
# my_list = [2, 3, 'ssafy', 4, 5]
# index = my_list.index(2)
# print(index) #0 

# # count 
# my_list = [1, 3, 2, 2, 3, 1, 3]
# count_num = my_list.count(3)
# print(count_num) # 3

# # sort 
# my_list = [3, 2, 1]
# my_list.sort()
# print(my_list) # [1, 2, 3]
# my_list.sort(reverse=True)
# print(my_list) # [3, 2, 1]

# # reverse
# my_list = [1, 3, 2, 8, 1, 9]
# my_list.reverse()
# print(my_list) # [9, 1, 8, 2, 3, 1]


# a = [1, 2, 3, 4]
# b = a 

# a[0] = 100

# print(a) 
# print(b)


# a = 100
# b = a

# b = 9

# print(a)
# print(b)

# # 할당 
# original_list = [1, 2, 3, 4]
# copy_list = original_list

# copy_list[0] = 'hello'
# print(original_list) # ['hello', 2, 3, 4]

# # 얕은 복사 
# a = [1, 2, 3]
# # 슬라이싱 - 잘라서 새로운 리스트로 반환 - 주소가 완전히 다른 리스트다 
# b = a[:]

# b[0] = 100

# print(a) # [1, 2, 3]
# print(b) # [100, 2, 3] 

# # 얕은 복사의 한계
# a = [1, 2, [100, 200]]
# b = a[:]

# b[2][0] = 999
# print(a) # [1, 2, [999, 200]]
# print(b) # [1, 2, [999, 200]]

import copy 

original_list = [1, 2, [1, 2]]
copied_list = copy.deepcopy(original_list)
copied_list[2][0] = 999

print(original_list) # [1, 2, [1, 2]]
print(copied_list) # [1, 2, [999, 2]]