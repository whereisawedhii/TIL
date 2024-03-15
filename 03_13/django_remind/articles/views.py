from django.shortcuts import render

# Create your views here.
def hello(request, num1, num2):
    result = num1 + num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
    }

    return render(request, "articles/hello.html", context)

def 함수(request):
    status = ['배','고','픈','재','성']
    context = {
        'message' : status
    }
    return render(request, 'articles/함수.html', context)