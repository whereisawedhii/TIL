from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def recommend(request):
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

    book_info = []
    for each in result:
        tmp = [each.get('책 제목'), each.get('저자')]
        book_info.append(tmp)

    context = {
        'book_info': book_info
    }

    return render(request, 'recommend.html', context)