import requests
from pprint import pprint as print


def author_works():
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
    works_title = [each['title'] for each in response['item']]
    
    return works_title


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    print(author_works())
