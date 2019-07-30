from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
# Create your views here.


def home(request):
    blogs = Blog.objects  # 쿼리셋 : 객체들의 목록을 알 수 있음 # 메소드
    return render(request, 'home.html', {'blogs': blogs})
    # blogs 키값


# 쿼리셋과 메소드의 형식
# 모델.쿼리셋(objects).메소드


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)

    return render(request, 'detail.html', {'blog': blog_detail})


def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET["title"]
    blog.body = reqeust.GET["body"]
    blog.save()


def new(request):
    return render(request, 'new.html')


def create(request):
    blog = Blog()
    blog.title = request.GET['title']
    blog.pub_date = timezone.datetime.now()
    blog.body = request.GET['body']
    blog.save()  # 쿼리셋 blog 객체를 저장해라
    return redirect('/blog/'+str(blog.id))
