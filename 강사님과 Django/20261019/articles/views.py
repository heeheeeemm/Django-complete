from django.shortcuts import render, redirect

# Create your views here.

# 현재 티렉토리에서 models.py로부터 Aritlce모델 가져오겠다.
from .models import Article

def index(request):
    # QuerySet API ---> 전체 데이터 조회
    # Article.objects.all()
    articles = Article.objects.all()

    context = {
        'articles': articles
    }
    # articles폴더의 index.html 파일을 랜더링하겠다
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API ---> 단일 게시글 조회 : get
    article = Article.objects.get(pk = pk)

    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

from django.shortcuts import render, redirect

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    # ORM중에 CREATE의 3가지 방법
    # POST : POST 방식, .get : 딕셔너리 메서드
    title = request.POST.get('title')
    content = request.POST.get('content')
    # 저장은 2번 방법 (유효성 검사!!)
    article = Article(title = title, content = content)
    # 데이터 관리 원칙 : 안정성, 보안성
    # save하기전에 반드시 유효성 검사를 해야한다!!
    article.save()
    return redirect('articles:detail', article.pk)

# CREATE와 차이는 전에 있던 게시글 조회
def edit(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article': article
    }
    return render(request, 'articles/edit.html', context)

# 리다이렉트 : (CREATE와 차이 : 기존에 있던 게시글을 변경)
def update(request, pk):
    article = Article.objects.get(pk = pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)


# POST요청 -> 리다이렉트
def delete(request, pk):
    # 조회후 삭제
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')