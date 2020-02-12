from django.shortcuts import render, redirect
from django.http import HttpResponse
from lotto.models import GuessNumbers
from lotto.forms import PostForm
# import 빠뜨리지 말 것!

# Create your views here.
def index(request):
    # site_1\lotto\templates\lotto\default.html
    # ex> 왜 굳이 templates 안에 또 lotto 파일을 만드는가?
    # site_1\member\templates\index.html
    # site_1\products\templates\index.html
    # site_1\history\templates\index.html
    # 이렇게 해놓을 경우 django가 멋대로 templates 폴더를 만들어 index 파일을 다 모아버린다!
    # => templates\index.html,index.html,index.html..
    lottos = GuessNumbers.objects.all()
    return render(request,'lotto/default.html', {'lottos':lottos})

def hello(request):
    return HttpResponse("<h1 style='color:blue;'>Hello, world!</h1>")

def post(request):
    print("*****")
    print(request.method)
    print("*****")

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            lotto = form.save(commit=False) # default=True, Github에서의 commit에 해당
            lotto.generate()
            return redirect('index')

    else:# GET 요청
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):
    lotto = GuessNumbers.objects.get(pk=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
