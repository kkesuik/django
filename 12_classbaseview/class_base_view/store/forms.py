from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    class Meta:
        model = Book
        fields = ['name', 'description', 'price']
        labels = {
            'name': '書籍名',
            'description': '説明',
            'price':'価格',
        }