# Generated by Django 3.2 on 2023-04-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20230410_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Побед хозяев'), (2, 'Побед гостей')], default=1),
        ),
    ]
