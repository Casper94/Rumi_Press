import decimal

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category, Books
import pandas as pd
import requests, decimal


class ExcelImportView(View):
    template_name = 'core/import.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        file_link = request.POST.get('excel_link')
        file_upload = request.FILES.get('excel_file')

        if file_link:
            response = requests.get(file_link)
            if response.status_code == 200:
                df = pd.read_excel(response.content)
                self.import_data(df)
                return render(request, self.template_name, {'success': True})
            else:
                return render(request, self.template_name, {'error': 'Failed to download the file.'})

        elif file_upload:
            df = pd.read_excel(file_upload)
            self.import_data(df)
            return render(request, self.template_name, {'success': True})

        else:
            return render(request, self.template_name, {'error': 'No link or file provided.'})

    def import_data(self, df):
        for _, row in df.iterrows():
            category, created = Category.objects.get_or_create(name=row['category'])
            obj = Books(
                id=row['id'],
                title=row['title'],
                subtitle=row['subtitle'],
                authors=row['authors'],
                publisher=row['publisher'],
                published_date=row['published_date'],
                category=category,
                distribution_expense= row['distribution_expense'],
            )

            obj.save()


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
    template_name = 'core/category_delete.html'
    success_url = reverse_lazy('category-list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return self.redirect(self.get_success_url())


class AddBooksView(CreateView):
    model = Books
    fields =['id', 'title', 'subtitle', 'authors',  'publisher', 'category', 'published_date',
             'distribution_expense']
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


class DetailBooksView(DetailView):
    model = Books
    template_name = 'core/books_detail.html'
    # context_object_name = 'books_de'


class UpdateBooksView(UpdateView):
    model = Books
    fields =['id', 'title', 'subtitle', 'authors',  'publisher', 'category', 'published_date', 'distribution_expense']
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
