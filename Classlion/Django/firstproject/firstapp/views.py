from django.shortcuts import render

# Create your views here. 파이썬 함수 식으로 적기
def welcome(request): #함수이름 
    return render(request, "welcome.html") #다른곳에서 welcome이라는 함수 요청하면 render라는 함수로 welcome.html 페이지를 띄워줌

def hello(request):
    userName = request.GET['name']
    return render(request, 'hello.html',{'userName' : userName})

