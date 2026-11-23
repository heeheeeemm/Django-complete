from django.shortcuts import render,redirect

# articles 할 때는 ModelForm을 사용했었음
# auth할 때는 built-in form을 사용할 거임
from django.contrib.auth.forms import (
    AuthenticationForm, #- 로그인을 위한 폼
    UserCreationForm,  #- 계정 생성을 위한 폼(회원가입)
    PasswordChangeForm,   #- 비밀번호 변경을 위한 폼
)

# 로그인, 로그아웃 기능
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import User

# 로그인 페이지를 띄우고 아이디/패스워드 입력하고 로그인 버튼을 누른다
def login(request):
    # 로그인 버튼 누른다
    if request.method == 'POST':   #- 로그인이 왜 post 요청이야?
        # AuthenticationForm : built-in form
        # request.POST -> (사용자가 입력한)아이디, 패스워드
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # get_user() : 인증된 사용자의 객체
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else: # GET요청 X (POST요청이 아닐 때)
        form = AuthenticationForm()   #- 빈 폼

    # Get 요청 or 유효성 검사가 실패했을 때 
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

from django.contrib.auth.decorators import login_required

# 로그인한 사용ㅇ자만 로그아웃할 수 있도록
@login_required
def logout(request):
    auth_logout(request)
    # 로그아웃 페이지가 따로 있나요? -> 없음
    return redirect('articles:index')

from .forms import CustomUserCreationForm

def signup(request):
    print(1)
    # is_  : True/False를 알려줭
    # is_authenticated : 인증된 사용자라면 (이미 회원가입이 되어 있다면)
    if request.user.is_authenticated :
        return redirect('articles:index')

    if request.method == 'POST':   #- submit 버튼 눌렀을 때
        # request.POST -> 내가 회원가입 할 때 입력한 정보들
        form = CustomUserCreationForm()
        if form.is_valid():   #1. 유효성 검사
            user = form.save()   #2. DB에 저장
            auth_login(request, user)    #3. 로그인
            return redirect('articles:index')

    else: # POST 요청이 아닐 때
        print(2)
        form = CustomUserCreationForm() # 빈 폼
    # 유효성 검사에 실패했다 or 
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)