from django import forms
from .models import Blog    # 같은 폴더의 models에서 클래서 Blog를 가져온다.

class BlogPost(forms.Form):
    email = forms.EmailField()
    files = forms.FileField()
    url = forms.URLField()
    words = forms.CharField(max_length = 200)
    max_number = forms.ChoiceField(choices = [('1','one'), ('2','two'), ('3','three')])
    # class Meta:
    #     model = Blog    #Blog를 기반으로한 모델
    #     fields = ['title','body']   #title과 body를 입력받고 싶다
    