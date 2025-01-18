# Generated by Django 5.1.4 on 2025-01-18 19:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='tournament_images', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Соревнование',
                'verbose_name_plural': 'Соревнования',
                'db_table': 'tournament',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='team_images')),
                ('id_tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
            ],
            options={
                'verbose_name': 'Команду',
                'verbose_name_plural': 'Команды',
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='TournamentAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_criterion', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
                ('id_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
                ('id_tournament', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.tournament')),
            ],
            options={
                'verbose_name': 'Критерий',
                'verbose_name_plural': 'Критерии',
                'db_table': 'tournament_assessment',
            },
        ),
        migrations.CreateModel(
            name='TournamentRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_members_in_team', models.IntegerField(verbose_name='Мин. кол-во участников в команде')),
                ('max_members_in_team', models.IntegerField(verbose_name='Макс. кол-во участников в команде')),
                ('date_start', models.DateField(verbose_name='Дата начала')),
                ('date_end', models.DateField(verbose_name='Дата окончания')),
                ('id_tournament', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.tournament', verbose_name='Соревнование')),
            ],
            options={
                'verbose_name': 'Правило',
                'verbose_name_plural': 'Правила',
                'db_table': 'tournament_rules',
            },
        ),
    ]
