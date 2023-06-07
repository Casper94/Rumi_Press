from import_export import resources
from .models import Category, Books


class EmployeeResource(resources.ModelResource):
    class Meta:
        model = Books