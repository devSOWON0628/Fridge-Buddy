# Generated by Django 5.0.6 on 2024-06-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_ingredient_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='imgUrl',
            field=models.CharField(default='', max_length=200),
        ),
    ]
