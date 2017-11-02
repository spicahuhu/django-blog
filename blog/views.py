from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from blog.models import Category,Tag,Article


def hello(request):
    context = {}
    context['hello'] = "hello qingchen!!!"
    return render(request, 'hello.html', context)
    # posts = BlogBodyPost.objects.all()
    # t = loader.get_template('content.html')
    # c = Context({'posts':posts})
    # return HttpResponse(t.render(c))
    # return HttpResponse('HELLO qingchen')

def index(request):
    # tags =Tag.objects.get(id=1)
    # articles = Article.objects.all()
    # cates = Category.objects.all()
    return render(request,'index.html')


def content(request, pk):
    info = get_object_or_404(Article, pk=pk)
    return render(request, 'single.html', context={'data': info})

def aboutMe(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
