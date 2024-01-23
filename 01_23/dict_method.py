
# clear
dict = {
    'name' : 'Alice', 
    'age' : 25
    }
# dict.clear()
# print(dict) # {}

# # get
# dict = {'name' : 'Alice', 'age' : 25}

# print(dict.get('name')) # 'Alice'
# print(dict['name']) # 'Alice' - 같은 값을 반환하지만, 키가 없을 때 얘는 에러남

# print(dict.get('country')) # None
# print(dict.get('country', 'unknown')) #'unknown'

# # keys
# print(dict.keys()) # dict_keys(['name', 'age']) 
# # 파이썬 내부적으로 키를 모은 데이터 타입 - 대괄호로 묶여있음 - 반복이 가능한 객체임
# for key in dict.keys() : 
#     print(key) # 'name'\n'age'

# # values
# print(dict.values()) # dict_values(['Alice', 25])

# for value in dict.values() :
#     print(value) # 'Alice'\n'25'

# # items
# print(dict.items()) # dict_items([('name', 'Alice'), ('age', 25)])

# for key, value in dict.items() : # 언패킹
#     print(key, value) # 'name Alice'\n'age 25'

# pop 
# print(dict.pop('age')) # 25
# print(dict) # {'name': 'Alice'}

# print(dict.pop('country')) #KeyError
# print(dict.pop('country', None)) # None

# setdefault 
print(dict.setdefault('country', 'Korea')) # Korea
print(dict) # {'name': 'Alice', 'age': 25, 'country': 'Korea'}

# update 
other = {'name': 'Jane', 'gender': 'Female'}

dict.update(other) # 겹치는건 덮어씌우고 나머지는 추가됨
print(dict) # {'name': 'Jane', 'age': 25, 'country': 'Korea', 'gender': 'Female'}

dict.update(age=50, country='Brazil')
print(dict) # {'name': 'Jane', 'age': 50, 'country': 'Brazil', 'gender': 'Female'}
