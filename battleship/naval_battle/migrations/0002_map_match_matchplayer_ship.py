# Generated by Django 5.0.2 on 2024-02-24 18:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('naval_battle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ships', models.JSONField(default=list)),
                ('shots', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', 'PENDING'), ('in_progress', 'IN_PROGRESS'), ('completed', 'COMPLETED')], default='pending', max_length=20)),
                ('moves_history', models.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='MatchPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='naval_battle.match')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='naval_battle.userprofile')),
                ('player_map', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='naval_battle.map')),
            ],
        ),
        migrations.CreateModel(
            name='Ship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_type', models.CharField(choices=[('destroyer', 'Destroyer'), ('submarine', 'Submarine'), ('cruiser', 'Cruiser'), ('battleship', 'Battleship'), ('carrier', 'Carrier')], default='destroyer', max_length=10)),
                ('status', models.CharField(choices=[('intact', 'Intact'), ('damaged', 'Damaged'), ('destroyed', 'Destroyed')], default='intact', max_length=9)),
                ('position', models.JSONField(default=list)),
                ('map', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ship_set', to='naval_battle.map')),
            ],
        ),
    ]