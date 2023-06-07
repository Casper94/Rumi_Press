from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Books


# Create your views here.
class Index(TemplateView):
    template_name = 'core/index.html'


class AddCategoryView(CreateView):
    model = Category
    fields =['name']
    template_name = 'core/category_add.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        entered_item = form.cleaned_data['name']
        item_exists = Category.objects.filter(name__iexact=entered_item).exists()
        if item_exists:
            error_message = 'Error adding the category. The entered categeory already exists. '
            return render(self.request, self.template_name, {'form': form,'error_message': error_message})
        else:
            form.instance.name = form.cleaned_data['name'].capitalize()
            return super().form_valid(form)


class ListCategoryView(ListView):
    model = Category
    template_name = 'core/category_list.html'
    context_object_name = 'category_list'
    ordering = ['name']
    paginate_by = 10


class UpdateCategoryView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'core/category_update.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        entered_item = form.cleaned_data['name']
        item_exists = Category.objects.filter(name__iexact=entered_item).exists()
        if item_exists:
            error_message = 'Error adding the category. The entered categeory already exists. '
            return render(self.request, self.template_name, {'form': form, 'error_message': error_message})
        else:
            form.instance.name = form.cleaned_data['name'].capitalize()
            return super().form_valid(form)


class DeleteCategoryView(DeleteView):
    model = Category
    fields = ['name']
    template_name = 'core/category_delete.html'
    success_url = reverse_lazy('category-list')


class AddBooksView(CreateView):
    model = Books
    fields =['id', 'title', 'subtitle', 'authors',  'publisher', 'category', 'published_date', 'distribution_expense']
    template_name = 'core/books_add.html'
    success_url = reverse_lazy('books-list')

    def form_valid(self, form):
        form.instance.title = form.cleaned_data['title'].capitalize()
        return super().form_valid(form)

class ListBooksView(ListView):
    model = Books
    template_name = 'core/books_list.html'
    context_object_name = 'books_list'
    ordering = ['title']
    paginate_by = 10


class UpdateBooksView(UpdateView):
    model = Books
    fields = ['name']
    template_name = 'core/books_update.html'
    success_url = reverse_lazy('books-list')

    def form_valid(self, form):
        form.instance.title = form.cleaned_data['title'].capitalize()
        return super().form_valid(form)


class DeleteBooksView(DeleteView):
    model = Books
    fields = ['name']
    template_name = 'core/books_delete.html'
    success_url = reverse_lazy('books-list')
