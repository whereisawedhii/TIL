import requests
from django.shortcuts import render
from pprint import pprint as print

API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
API_KEY = 'ttbzsm12301129001'

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'ItemNewSpecial',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()

    result = []
    for item in response['item']:
        info = {
            'isbn': item['isbn'],
            'title': item['title'],
            'pubDate': item['pubDate'],
            'author': item['author'],

        }
        result.append(info)
    context = {
        'result': result
    }
    return render(request, 'recommend.html', context)

def bestseller(request):
    params = {
        'ttbkey': API_KEY,
        'QueryType': 'Bestseller',
        'MaxResults': '50',
        'start': '1',
        'SearchTarget': 'Book',
        'output': 'js',
        'Version': '20131101'
    }

    response = requests.get(API_URL, params=params).json()
    print(response)

    result = []
    for item in response['item']:
        if 'bestDuration' in item.keys():
            info = [item['salesPoint']]
            tmp = {
                'isbn': item['isbn'],
                'title': item['title'],
                'pubDate': item['pubDate'],
                'author': item['author'],
                'bestDuration': item['bestDuration'],
            }
            info.append(tmp)
            result.append(info)
    
    result.sort(key=lambda x: x[0], reverse=True)

    book_info = []
    for each in result:
        book_info.append(each[1])

    context = {
        'book_info': book_info
    }
    return render(request, 'bestseller.html', context)