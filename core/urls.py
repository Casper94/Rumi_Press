from django.contrib import admin
from django.urls import path
from .views import Index, AddCategoryView, ListCategoryView, UpdateCategoryView, DeleteCategoryView, \
    AddBooksView, ListBooksView, UpdateBooksView, DeleteBooksView, DetailBooksView, ExcelImportView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("import/", ExcelImportView.as_view(), name="excel_import"),
    path("category/", ListCategoryView.as_view(), name="category-list"),
    path("category/add/", AddCategoryView.as_view(), name="category-add"),
    path("category/<pk>/update/", UpdateCategoryView.as_view(), name="category-update"),
    path("category/<pk>/delete/", DeleteCategoryView.as_view(), name="category-delete"),
    path("books/", ListBooksView.as_view(), name="books-list"),
    path("books/add/", AddBooksView.as_view(), name="books-add"),
    path("books/<pk>/detail/", DetailBooksView.as_view(), name="books-detail"),
    path("books/<pk>/update/", UpdateBooksView.as_view(), name="books-update"),
    path("books/<pk>/delete/", DeleteBooksView.as_view(), name="books-delete"),

]
