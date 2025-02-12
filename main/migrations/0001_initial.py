# Generated by Django 5.1.6 on 2025-02-12 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'db_table': 'tournament_category',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/tournament_logo', verbose_name='Логотип')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to='main.categorytournament')),
            ],
            options={
                'verbose_name': 'Соревнование',
                'verbose_name_plural': 'Соревнования',
                'db_table': 'tournament',
                'ordering': ('-date_added',),
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/team_logo', verbose_name='Логотип')),
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
