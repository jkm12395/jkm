from django.shortcuts import render, redirect, reverse

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Book, Hero

from django.http import HttpResponseRedirect


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


def deletebook(request, bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # return HttpResponse("删除成功")
    url = reverse("booktest:index")
    # return HttpResponseRedirect(redirect_to='/')
    return redirect(to=url)


def addhero(request, bookid):
    if request.method == "GET":
        return render(request, 'addhero.html')
    elif request.method == "POST":
        hero = Hero()
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.gender = request.POST.get("sex")
        hero.book = Book.objects.get(id=bookid)
        hero.save()
        url = reverse("booktest:addhero", args=(bookid,))
        return redirect(to=url)


def deletehero(request, heroid):
    hero = Hero.objects.get(id=heroid)
    bookid = hero.bookid
    hero.delete()
    url = reverse("booktest:detail", args=(bookid,))
    return redirect(to=url)


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
