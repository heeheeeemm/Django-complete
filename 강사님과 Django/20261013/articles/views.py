from django.shortcuts import render

# Create your views here.

def index(request):

    # context 딕셔너리 구조
    # templates(.html)에서 context의 key로 접근하면 value값을 가져올 수 있음
    context = {
        'name' : 'Jane', 
        'number' : 1
    }
    return render(request, 'articles/index.html', context)
