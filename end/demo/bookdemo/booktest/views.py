from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Book, Hero


def index(request):
    # return HttpResponse("这里是首页")
    # 1,获取模板
    # template = loader.get_template('index.html')
    # 2,渲染模板数据
    books = Book.objects.all()
    # context = {"books": books}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request, 'index.html', {"books": books})


def about(request):
    return HttpResponse("这里是关于页")


def detail(request, bookid):
    # return HttpResponse("这里是关于详情页" + bookid)
    # template = loader.get_template('detail.html')
    book = Book.objects.get(id=bookid)
    # context = {"book": book}
    # result = template.render(context)
    # return HttpResponse(result)

    return render(request, 'detail.html', {"book": book})