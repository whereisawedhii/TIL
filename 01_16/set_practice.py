my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

#합집합
print(my_set_1 | my_set_2) # {1, 2, 3, 6, 9}
#차집합
print(my_set_1 - my_set_2) # {1, 2}
#교집합
print(my_set_1 & my_set_2) # {3}