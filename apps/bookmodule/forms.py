from django import forms
from .models import Book, Student, Student2, ProductImage
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(AuthenticationForm):
    pass