import requests
from pprint import pprint


def best_review_books():
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
    works_title = [each for each in response['item'] if each['customerReviewRank'] >= 9 ]

    return works_title

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(best_review_books())
