from django.shortcuts import render

# Create your views here.
def index(request):
    work = request.GET.get('work')
    if not work:
        work = '아직 할 일이 없습니다.'
    context = {
        'work': work
    }
    return render(request, 'todos/index.html', context)

def detial_view(request, work):
    context = {
        'work':work
    }
    return render(request, 'todos/detail.html', context)

def create_todo(request):
    return render(request, 'todos/create_todo.html')