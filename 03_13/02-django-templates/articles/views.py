import random
from django.shortcuts import render


# Create your views here.
def index(request):
    context = {
        'name': '정연'
    }
    return render(request, 'articles/index.html', context)


def dinner(request):
    foods = [
        '국밥',
        '국수',
        '카레',
        '탕수육',
    ]
    picked = random.choice(foods)
    
    context = {

        'foods': foods,
        'picked': picked,
    }
    return render(request, 'articles/dinner.html', context)

def search(request):
    return render(request, 'articles/search.html')

def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # print(request)
    # print(type(request))
    # print(dir(request))
    # print(request.GET)   
    # print(request.GET.get('message'))   #hello
    message = request.GET.get('query')

    # throw 페이지에서 데이터를 받고 
    # 그 안에서 사용자 입력 데이터를 추출하고
    # template에 그대로 출력해야함 
    context = {
        'message':message
    }
    return render(request, 'articles/catch.html', context)

def greeting(request, name):
    context = {
        'name':name
    }
    return render(request, 'articles/greeting.html', context)