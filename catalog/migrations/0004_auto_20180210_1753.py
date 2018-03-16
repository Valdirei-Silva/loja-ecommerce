# Generated by Django 2.0.1 on 2018-02-10 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='caption',
            field=models.TextField(blank=True, max_length=150, verbose_name='Legenda'),
        ),
        migrations.AddField(
            model_name='product',
            name='in_promotion',
            field=models.BooleanField(default=False, verbose_name='Em promoção'),
        ),
    ]