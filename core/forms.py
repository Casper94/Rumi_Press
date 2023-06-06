from django import forms

class AddCategoryForm(forms.Form):
    name = forms.CharField()
    pass