# Generated by Django 5.0.6 on 2024-06-02 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_user_ingredient_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='unit',
            field=models.IntegerField(choices=[(1, 'G'), (2, '개')], null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
