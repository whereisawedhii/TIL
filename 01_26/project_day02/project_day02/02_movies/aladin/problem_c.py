import requests
from pprint import pprint


def bestseller_book():
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params = {
        'ttbkey': 'ttbzsm12301129001',
        'Query': '파울로 코엘료',
        'QueryType': 'author',
        'MaxResults': 20,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response = requests.get(URL, params=params).json()

    works_dict = {}
    salesPoint = []
    for each in response['item'] : 
        works_dict[each['salesPoint']] = each['title']
        salesPoint.append(each['salesPoint'])

    salesPoint.sort(reverse=True)
    bestseller = [ works_dict[salesPoint[i]] for i in range(5) ]

    return bestseller


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(bestseller_book())
