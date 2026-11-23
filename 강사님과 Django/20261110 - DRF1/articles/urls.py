from django.urls import path
from articles import views

# app_name 쓸까? 왜안쓸까? templates 없다.

urlpatterns = [
    # 전체 게시글 조회, 게시글 생성
    path('articles/', views.article_list),
    # 단일 게시글 조회, 게시글 삭제, 게시글 수정
    path('articles/<int:article_pk>/', views.article_detail),

]
