# views.py
from django.shortcuts import render


# Create your views here.
# 메인 페이지를 만드는 index라는 이름의 함수를 작성
def index(request):
    return render(request, 'articles/index.html')
# render(요청객체, 템플릿 이후 경로)
# templates 이후의 경로가 들어감