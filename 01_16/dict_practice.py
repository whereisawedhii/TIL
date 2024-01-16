my_dict = {
    'apple': 100, 
    'list': [1, 2, 3],
    'apple' : 12
}

print(my_dict)

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]

# 값은 변경-재할당 가능 
my_dict['apple'] = 100
print(my_dict) # {'apple': 100, 'list': [1, 2, 3]}

