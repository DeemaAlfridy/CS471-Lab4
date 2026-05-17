from django.shortcuts import render, redirect
from .models import BookLab, Publisher, Book, Student, Student2, Address
from django.db.models import Sum, F, FloatField, ExpressionWrapper, Min, Max, Avg, Count, Q
from .forms import BookForm, StudentForm, Student2Form, ProductImageForm

def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, "bookmodule/links.html")

def formatting(request):
    return render(request, "bookmodule/formatting.html")

def listing(request):
    return render(request, "bookmodule/listing.html")

def tables(request):
    return render(request, "bookmodule/tables.html")

def __getBooksList():
    book1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J.Humble and D. Farley'}
    book2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    book3 = {'id': 43211234, 'title': 'The Hundred-Page Machine Learning Book', 'author': 'Andriy Burkov'}
    return [book1, book2, book3]

def search_view(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        # filter books
        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')
from django.shortcuts import render
from .models import Book

def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})

def complex_query(request):
    mybooks = Book.objects.filter(
        author__isnull=False
    ).filter(
        title__icontains='and'
    ).filter(
        edition__gte=2
    ).exclude(
        price__lte=40
    )[:10]

    if len(mybooks) >= 1:
        return render(request, 'bookmodule/bookList.html', {'books': mybooks})
    else:
        return render(request, 'bookmodule/index.html')
    
from django.db.models import Q
def task1(request):
    books = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/task1.html', {'books': books})
def task2(request):
    books = Book.objects.filter(
        Q(edition__gt=3) & 
        (Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task2.html', {'books': books})
def task3(request):
    books = Book.objects.filter(
        Q(edition__lte=3) &
        ~(Q(title__icontains='qu') | Q(author__icontains='qu'))
    )
    return render(request, 'bookmodule/task3.html', {'books': books})
def task4(request):
    books = Book.objects.all().order_by('-title') 
    return render(request, 'bookmodule/task4.html', {'books': books})
from django.db.models import Avg, Sum, Max, Min, Count

def task5(request):
    stats = Book.objects.aggregate(
        count=Count('id'),
        total_price=Sum('price'),
        avg_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price')
    )
    return render(request, 'bookmodule/task5.html', {'stats': stats})

from django.db.models import Count
from .models import Student
def task7(request):
    data = Student.objects.values('address__city').annotate(count=Count('id'))
    return render(request, 'bookmodule/task7.html', {'data': data})

def lab9_task1(request):
    total = BookLab.objects.aggregate(total=Sum('quantity'))['total'] or 1

    books = BookLab.objects.annotate(
        percentage=ExpressionWrapper(
            (F('quantity') * 100.0) / total,
            output_field=FloatField()
        )
    )

    return render(request, 'bookmodule/lab9_task1.html', {'books': books})

def lab9_task2(request):
    publishers = Publisher.objects.annotate(
        total_books=Sum('booklab__quantity')
    )

    return render(request, 'bookmodule/lab9_task2.html', {'publishers': publishers})
def lab9_task3(request):
    publishers = Publisher.objects.annotate(
        oldest_book=Min('booklab__pubdate')
    )

    return render(request, 'bookmodule/lab9_task3.html', {'publishers': publishers})

def lab9_task4(request):
    publishers = Publisher.objects.annotate(
        avg_price=Avg('booklab__price'),
        min_price=Min('booklab__price'),
        max_price=Max('booklab__price')
    )

    return render(request, 'bookmodule/lab9_task4.html', {'publishers': publishers})
def lab9_task5(request):
    publishers = Publisher.objects.annotate(
        high_rated_books=Count(
            'booklab',
            filter=Q(booklab__rating__gte=4)
        )
    )

    return render(request, 'bookmodule/lab9_task5.html', {'publishers': publishers})
def lab9_task6(request):
    publishers = Publisher.objects.annotate(
        filtered_books=Count(
            'booklab',
            filter=Q(
                booklab__price__gt=50,
                booklab__quantity__gte=1,
                booklab__quantity__lt=5
            )
        )
    )

    return render(request, 'bookmodule/lab9_task6.html', {'publishers': publishers})
def list_books_lab10(request):
    books = Book.objects.all()
    return render(request, 'bookmodule/lab10_list.html', {'books': books})
def add_book_lab10(request):

    if request.method == 'POST':

        title = request.POST['title']
        author = request.POST['author']

        Book.objects.create(
            title=title,
            author=author
        )

    return render(request, 'bookmodule/lab10_addbook.html')
def edit_book_lab10(request, id):

    book = Book.objects.get(id=id)

    if request.method == 'POST':

        book.title = request.POST['title']
        book.author = request.POST['author']

        book.save()

    return render(request,
                  'bookmodule/lab10_editbook.html',
                  {'book': book})
def delete_book_lab10(request, id):

    book = Book.objects.get(id=id)

    book.delete()

    return redirect('/books/lab10_part1/listbooks')
def add_book_form(request):

    if request.method == 'POST':

        form = BookForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/books/lab10_part1/listbooks')

    else:

        form = BookForm()

    return render(request,
                  'bookmodule/book_form.html',
                  {'form': form})

def lab11_students(request):

    students = Student.objects.all()

    return render(
        request,
        'bookmodule/lab11_students.html',
        {'students': students}
    )

def lab11_add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/books/lab11/students/')

    else:

        form = StudentForm()

    return render(
        request,
        'bookmodule/lab11_add_student.html',
        {'form': form}
    )

def lab11_edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == 'POST':

        form = StudentForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            return redirect('/books/lab11/students/')

    else:

        form = StudentForm(instance=student)

    return render(
        request,
        'bookmodule/lab11_add_student.html',
        {'form': form}
    )


def lab11_delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect('/books/lab11/students/')

def lab11_task2_students(request):

    students = Student2.objects.all()

    return render(
        request,
        'bookmodule/lab11_task2_students.html',
        {'students': students}
    )


def lab11_task2_addstudent(request):

    if request.method == 'POST':

        form = Student2Form(request.POST)

        if form.is_valid():

            form.save()

            return redirect('/books/lab11/task2/students/')

    else:

        form = Student2Form()

    return render(
        request,
        'bookmodule/lab11_task2_addstudent.html',
        {'form': form}
    )

def lab11_task3_add_image(request):

    if request.method == 'POST':

        form = ProductImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

    else:
        form = ProductImageForm()

    return render(request,
                  'bookmodule/lab11_add_image.html',
                  {'form': form})