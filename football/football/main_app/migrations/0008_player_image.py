# Generated by Django 3.2 on 2023-04-10 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_auto_20230410_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
