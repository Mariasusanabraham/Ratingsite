# Generated by Django 3.2.7 on 2021-10-01 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ratingapp', '0004_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Description',
            field=models.TextField(),
        ),
    ]