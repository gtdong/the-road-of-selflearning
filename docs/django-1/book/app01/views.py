from django.shortcuts import render,redirect,HttpResponse
from app01 import models

# Create your views here.

def add(request):
    if request.method == 'POST':
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        press = request.POST.get('press')
        models.Book.objects.create(bookname=bookname,author=author,press=press)
        return redirect('/book_list')

    return render(request,'add.html')

def list(request):
    data = models.Book.objects.all()

    return render(request,'list.html',locals())

def delete(request):
    delete_id = request.GET.get('id')
    models.Book.objects.filter(pk=delete_id).delete()

    return redirect('/book_list')

def edit(request):

    if request.method == 'POST':
        edit_id = request.GET.get('id')
        bookname = request.POST.get('bookname')
        author = request.POST.get('author')
        press = request.POST.get('press')

        models.Book.objects.filter(pk=edit_id).update(bookname=bookname,author=author,press=press)

        return redirect('/book_list')

    edit_id = request.GET.get('id')
    edit_obj = models.Book.objects.filter(pk=edit_id).first()
    return render(request,'edit.html',locals())