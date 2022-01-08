# Generated by Django 3.2.9 on 2022-01-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220107_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='year_warranty',
            field=models.CharField(choices=[('1', 'none'), ('2', '2 years'), ('3', '3 years'), ('5', '5 years'), ('l', 'life')], default='1', max_length=1),
        ),
    ]