import requests
from pprint import pprint as print

dummy_data = []
censored_user_list = {}

for i in range(1,11) :
    new_URL = 'https://jsonplaceholder.typicode.com/users/' + str(i)
    response = requests.get(new_URL)
    parsed_data = response.json()
    if float(parsed_data['address']['geo']['lat']) >= 80 or float(parsed_data['address']['geo']['lat']) <= -80 :
        continue
    if float(parsed_data['address']['geo']['lng']) >= 80 or float(parsed_data['address']['geo']['lng']) <= -80 :
        continue
    dict_1 = {}
    dict_1['company'] = parsed_data['company']['name']
    dict_1['lat'] = parsed_data['address']['geo']['lat']
    dict_1['lng'] = parsed_data['address']['geo']['lng']
    dict_1['name'] = parsed_data['name']
    dummy_data.append(dict_1)

black_list = [
    'Hoeger LLC',
    'Keebler LLC',
    'Yost and Sons',
    'Johns Group',
    'Romaguera-Crona',
]



def create_user(user_list):
    for each in user_list :
        censor = censorship(each['company'], each['name'])
        if censor == True :
             censored_user_list[each['company']] = [each['name']]

    return censored_user_list


def censorship(company, name):
        if black_list.count(company) != 0 :
            print(f'{company} 소속의 {name} 은/는 등록할 수 없습니다.')
            return False
        else :
            print('이상 없습니다.')
            return True 

print(create_user(dummy_data))