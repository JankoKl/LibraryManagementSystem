from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .api import BookViewSet, StudentViewSet, BookIssueViewSet, BookInstanceViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'students', StudentViewSet)
router.register(r'book-issues', BookIssueViewSet)
router.register(r'book-instances', BookInstanceViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new_student', views.add_new_student, name='new_student'),
    path('add_new_book', views.add_new_book, name='new_book'),
    path('add_book_issue', views.add_book_issue, name='book_issue'),
    path('add_new_book_instance', views.add_new_book_instance, name='add_new_book_instance'),
    path('show_students', views.view_students, name='show_student_record'),
    path('view_books', views.view_books, name='show_book_record'),
    path('view_books_issued', views.view_bissue, name='show_issue_record'),
    path('edit/student/<str:roll>', views.edit_student_data, name="Edit Student data"),
    path('edit/book/<uuid:id>', views.edit_book_data, name="Edit Book data"),
    path('delete/student/<str:roll>', views.delete_student, name="Delete Student data"),
    path('delete/book/<str:id>', views.delete_book, name="Delete book data"),
    path('return_book/<int:id>', views.return_issued_book, name="return_issued_book"),
    path('edit_issued/<int:id>', views.edit_issued, name="edit_issued"),
    path('register/', views.register, name='register'),
    path('api/', include(router.urls)),
]