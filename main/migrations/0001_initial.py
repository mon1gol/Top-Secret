# Generated by Django 5.1.2 on 2024-12-06 21:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hackathon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField()),
                ('logo', models.ImageField(upload_to=None)),
            ],
            options={
                'db_table': 'hackathon',
            },
        ),
        migrations.CreateModel(
            name='HackathonRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_members_in_team', models.IntegerField()),
                ('max_members_in_team', models.IntegerField()),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('id_hackathon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.hackathon')),
            ],
            options={
                'db_table': 'hackathon_rules',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to=None)),
                ('id_hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hackathon')),
            ],
            options={
                'db_table': 'team',
            },
        ),
        migrations.CreateModel(
            name='HackathonAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_criterion', models.CharField(max_length=50)),
                ('result', models.IntegerField()),
                ('id_hackathon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.hackathon')),
                ('id_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.team')),
            ],
            options={
                'db_table': 'hackathon_assessment',
            },
        ),
    ]
