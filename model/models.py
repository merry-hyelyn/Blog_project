from django.db import models

# Create your models here.

# 글 형식 지정 틀 생성

# 장고에서 DB에 접근하는 내장함수 = model


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    #타이틀의 내용이 목록에 뜨도록함
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]  # 파이썬 문법 참고
        # 본문 리턴 [:100] 100글자 상한선



