# Generated by Django 4.2.2 on 2023-08-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_books_distribution_expense'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(default='Untitled', max_length=50),
        ),
    ]
