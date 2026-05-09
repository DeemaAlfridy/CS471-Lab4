from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="books.index"),
    path('list_books/', views.list_books, name="books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('html5/links/', views.links, name="books.links"),
    path('html5/text/formatting/', views.formatting, name="books.formatting"),
    path('html5/listing/', views.listing, name="books.listing"),
    path('html5/tables/', views.tables, name="books.tables"),
    path('search/', views.search_view, name="books.search"),
    path('simple/query/', views.simple_query, name="books.simple_query"),
    path('complex/query/', views.complex_query, name="books.complex_query"),
    path('lab8/task1', views.task1, name='task1'),
    path('lab8/task2', views.task2, name='task2'),
    path('lab8/task3', views.task3, name='task3'),
    path('lab8/task4', views.task4, name='task4'),
    path('lab8/task5', views.task5, name='task5'),
    path('lab8/task7', views.task7, name='task7'),
    path('lab9/task1', views.lab9_task1),
    path('lab9/task2', views.lab9_task2),
    path('lab9/task3', views.lab9_task3),
    path('lab9/task4', views.lab9_task4),
    path('lab9/task5', views.lab9_task5),
    path('lab9/task6', views.lab9_task6),
    path('lab10_part1/listbooks', views.list_books_lab10),
    path('lab10_part1/addbook', views.add_book_lab10),
    path('lab10_part1/editbook/<int:id>', views.edit_book_lab10),
    path('lab10_part1/deletebook/<int:id>', views.delete_book_lab10),
    path('lab10_part2/addbook', views.add_book_form),
    ]

