import requests
from pprint import pprint


def author_other_works(title):
    # 여기에 코드를 작성합니다.
    URL = 'http://www.aladin.co.kr/ttb/api/ItemSearch.aspx'

    params1 = {
        'ttbkey': 'ttbzsm12301129001',
        'Query': {title},
        'QueryType': 'title',
        'MaxResults': 1,
        'start': 1,
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101',
    }

    response1 = requests.get(URL, params=params1).json()

    try : 
        author = response1['item'][0]['author']
        author1 = author.split(' (지은이)')

        params2 = {
            'ttbkey': 'ttbzsm12301129001',
            'Query': author1[0],
            'QueryType': 'author',
            'MaxResults': 5,
            'start': 1,
            'SearchTarget': 'Book',
            'output': 'js',
            'Version': '20131101',
        }

        response2 = requests.get(URL, params=params2).json()
        other_works = [each['title'] for each in response2['item']]
        return other_works
    except : 
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(author_other_works('베니스의 상인'))

    pprint(author_other_works('개미'))

    pprint(author_other_works('*'))
