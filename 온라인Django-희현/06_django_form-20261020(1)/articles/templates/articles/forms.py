from django import forms

class ArticleForm(forms.Form):
    # 사용자로부터 입력 받을 필드를 정의
    title = forms.CharField(max_length=10)
    content = forms.CharField(widget=forms.Textarea)