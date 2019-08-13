from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            # form 태그에서 name에 username이라고 되어있는 부분 post 방식으로 가져옴
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)  # 로그인 함수
            return redirect('home')
    return render(request, 'signup.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # DB에 저장된 내용과 같은 데이터가 있는지 확인하는 함수 #authenticate 결과를 user에 저장
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect'})
    return render(request, 'login.html')


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('home')
    return render(request, 'login.html')
