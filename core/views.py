from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Category


# Create your views here.
class Index(TemplateView):
    template_name = 'core/index.html'


class AddCategoryView(CreateView):
    model = Category
    fields =['name']
    template_name = 'core/add_category.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        entered_item = form.instance.name
        item_exists = Category.objects.filter(name=entered_item).exists()
        if item_exists:
            error_message = 'Error adding the category. The entered categeory already exists. '
            return render(self.request, self.template_name, {'form': form,'error_message': error_message})
        else:
            success_message = 'Category successfully created!'
            return super().form_valid(form)


class ListCategoryView(ListView):
    model = Category
    template_name = 'core/list_category.html'
    context_object_name = 'category_list'
    paginate_by = 10


class UpdateCategoryView(UpdateView):
    model = Category
    fields = ['name']
    template_name = 'core/add_category.html'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        entered_item = form.instance.name
        item_exists = Category.objects.filter(name=entered_item).exists()
        if item_exists:
            error_message = 'Error adding the category. The entered categeory already exists. '
            return render(self.request, self.template_name, {'form': form, 'error_message': error_message})
        else:
            success_message = 'Category successfully created!'
            return super().form_valid(form)