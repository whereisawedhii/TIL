import requests
from pprint import pprint


def ebook_list(title):
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
        price_paper =  response1.get('item')[0].get('priceSales')

        params2 = {
            'ttbkey': 'ttbzsm12301129001',
            'Query': {title},
            'QueryType': 'title',
            'MaxResults': 1,
            'start': 1,
            'SearchTarget': 'eBook',
            'output': 'js',
            'Version': '20131101',
        }
        response2 = requests.get(URL, params=params2).json()
        price_ebook =  response2.get('item')[0].get('priceSales')
        first_book = response2.get('item')[0]

        if price_paper * 0.9 > price_ebook :
            ebook_info = {}
            ebook_info['itemId'] = first_book['itemId']
            ebook_info['isbn'] = first_book['isbn']
            ebook_info['priceSales'] = first_book['priceSales']
            ebook_info['link'] = first_book['link']

        return [ebook_info]
    
    except : 
        return None

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(ebook_list('베니스의 상인'))

    pprint(ebook_list('*'))
