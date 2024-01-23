# my_set = {} # 빈 딕셔너리 

# my_set = {'a', 'b', 'c', 1, 2, 3} 
# print(my_set) # 세트는 순서가 존재하지 않음 {1, 2, 3, 'c', 'a', 'b'}

# # add 
# my_set.add(4) 
# print(my_set) # {'b', 1, 2, 3, 'c', 4, 'a'}

# # 중복이 되지 않음 
# my_set.add(4)
# print(my_set) # {'b', 1, 2, 3, 'c', 4, 'a'}

# # remove
# my_set.remove('a')
# print(my_set) # {1, 2, 3, 'c', 'b', 4}

# my_set.remove('z') # KeyError: 'z'

# # clear
# my_set.clear()
# print(my_set) # set() - 빈세트 출력

# # pop
# my_set = {'a', 'b', 'c', 1, 2, 3}
# element = my_set.pop()
# print(element) # random element 

# # update
# my_set = {'a', 'b', 'c', 1, 2, 3}
# my_set.update([1, 4, 5])
# print(my_set) # {1, 2, 3, 4, 5, 'a', 'b', 'c'}

# # discard
# my_set.discard(1)
# print(my_set) # {2, 3, 4, 'c', 5, 'a', 'b'}

# my_set.discard('z')
# print(my_set) #{2, 3, 4, 'c', 5, 'a', 'b'}

# difference
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2)) # {0, 2, 4}
print(set1 - set2) # {0, 2, 4}

# intersection
print(set1.intersection(set2)) # {1, 3}
print(set1 & set2) # {1, 3}

# issubset
print(set1.issubset(set2)) # False
print(set1 <= set2) # False

# issuperset
print(set1.issuperset(set2)) # False
print(set1 >= set2) # False
print(set1.issuperset(set3)) # True

# union
print(set1.union(set2)) # {0, 1, 2, 3, 4, 5, 7, 9}
print(set1 | set2) # {0, 1, 2, 3, 4, 5, 7, 9}


