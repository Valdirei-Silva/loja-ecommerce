# Generated by Django 2.0.1 on 2018-02-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20180107_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image_products', verbose_name='Imagem'),
        ),
    ]
