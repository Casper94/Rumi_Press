# Generated by Django 4.2.2 on 2023-06-07 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_books_authors_alter_books_distribution_expense_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='distribution_expense',
            field=models.FloatField(blank=True, null=True),
        ),
    ]