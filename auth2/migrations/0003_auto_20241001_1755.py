# Generated by Django 3.1.2 on 2024-10-01 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth2', '0002_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.DateField(),
        ),
    ]