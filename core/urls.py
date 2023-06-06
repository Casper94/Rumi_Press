from django.contrib import admin
from django.urls import path
from .views import Index, AddCategoryView, ListCategoryView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path("category/", ListCategoryView.as_view(), name="category-list"),
    path("category/add/", AddCategoryView.as_view(), name="category-add"),

]
