import requests
from pprint import pprint as print

API_URL = "http://www.aladin.co.kr/ttb/api/ItemList.aspx"
API_KEY = "ttbzsm12301129001"
params = {
    'TTBKey': API_KEY,
    'QueryType':'ItemNewSpecial',
    'MaxResults': 50,
    'SearchTarget':'Book',
    'Output': 'JS',
    'version':'20131101'
}

response = requests.get(API_URL, params=params).json()

result = []
for each in response['item']:
    tmp = {}
    tmp['책 제목'] = each['title']
    tmp['저자'] = each['author']
    tmp['출간일'] = each['pubDate']
    tmp['국제 표준 도서 번호'] = each['isbn']
    result.append(tmp)


print(result)