# Generated by Django 5.1.1 on 2024-10-23 06:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesapp', '0002_player_rename_winner_gameresult_result_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gameresult',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamesapp.player'),
        ),
    ]
