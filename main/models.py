from django.db import models


class Hackathon(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    logo = models.ImageField(upload_to='hackathon_images', blank=True, null=True, height_field=None, width_field=None, max_length=None, verbose_name='Логотип')

    class Meta:
        db_table = 'hackathon'
        verbose_name = 'Хакатон'
        verbose_name_plural = 'Хакатоны'


class HackathonRules(models.Model):
    min_members_in_team = models.IntegerField(verbose_name='Мин. кол-во участников в команде')
    max_members_in_team = models.IntegerField(verbose_name='Макс. кол-во участников в команде')
    date_start = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата начала')
    date_end = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата окончания')
    id_hackathon = models.OneToOneField(Hackathon, on_delete=models.CASCADE, verbose_name='Хакатон')

    class Meta:
        db_table = 'hackathon_rules'
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'


class HackathonAssessment(models.Model):
    name_criterion = models.CharField(max_length=50)
    result = models.IntegerField()
    id_hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    id_team = models.ForeignKey('Team', on_delete=models.CASCADE)

    class Meta:
        db_table = 'hackathon_assessment'
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='team_images', blank=True, null=True, height_field=None, width_field=None, max_length=None)
    id_hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    class Meta:
        db_table = 'team'
        verbose_name = 'Команду'
        verbose_name_plural = 'Команды'
    