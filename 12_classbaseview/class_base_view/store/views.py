from django.shortcuts import render
from django.views.generic.base import (
    View,TemplateView
)
from . import forms
from django.views.generic.detail import DetailView
from datetime import datetime
from .models import Book

# Create your views here.
class IndexView(View):
    
    #http_method_names=['@@@']を入れるとmethodを制限できる
     
     def get(self, request, *args, **kwargs):
        book_form = forms.BookForm()
        return render(request, 'index.html',context={
            'book_form': book_form,
        })    

     def post(self, request, *args, **kwargs):
        book_form = forms.BookForm( request.POST or None)
        if book_form.is_valid():
            book_form.save()
        return render( request, 'index.html', context={
            'book_form':book_form,
        })
        

class HomeView(TemplateView):
    
    template_name = 'home.html'
    extra_context = {
        'message':'ホームです'
    }
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['time']= datetime.now()
       context['name']=kwargs.get('name')#kwargsの中にurlで指定した値が入っている
       return context
    
class BookDetailView(DetailView):
    model = Book
    template_name = 'book.html'
    context_object_name = 'books'
    pk_url_kwarg = 'book_id'
    slug_field = 'name'
    queryset = Book.objects.filter(price__gt = 1000)#もともと絞り込める
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context.get('books')
        print(book)
        if book:
            context.update({
            'price_with_tax':book.price * 1.1
        })
        return context
    