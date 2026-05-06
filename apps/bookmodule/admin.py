from django.contrib import admin
from .models import Student, Address, Publisher, Author, BookLab


admin.site.register(Student)
admin.site.register(Address)

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(BookLab)