# Generated by Django 3.2.7 on 2021-10-01 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ratingapp', '0002_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='Image',
            field=models.CharField(default='', max_length=300),
        ),
    ]