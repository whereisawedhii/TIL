# 딕셔너리에서 키를 조회할 때 키가 없는 상황 
dict = {'condition' : 'hungry'}

# try - except
try :
    age = dict['age']
    print(age)
except :
    print('내 나이가 어때서')

# if - else 
if 'age' in dict :
    age = dict['age']
    print(age)
else : 
    print('내 나이가 어때서')