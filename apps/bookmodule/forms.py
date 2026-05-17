from django import forms
from .models import Book, Student, Student2, ProductImage


class BookForm(forms.ModelForm):

    class Meta:

        model = Book

        fields = ['title', 'author', 'price', 'edition']

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'


class Student2Form(forms.ModelForm):

    class Meta:

        model = Student2

        fields = '__all__'

class ProductImageForm(forms.ModelForm):

    class Meta:
        model = ProductImage
        fields = '__all__'