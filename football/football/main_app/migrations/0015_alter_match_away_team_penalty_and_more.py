# Generated by Django 4.2 on 2023-04-16 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_alter_match_away_team_penalty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='away_team_penalty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='home_team_penalty',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]