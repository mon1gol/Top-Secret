from django.db import models


class CategoryTournament(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField()

    class Meta:
        db_table = 'tournament_category'
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'
    

class Tournament(models.Model):
    category = models.ForeignKey(CategoryTournament, related_name='tournaments', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='Название')
    slug = models.SlugField()
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    logo = models.ImageField(upload_to='uploads/tournament_logo', blank=True, null=True, verbose_name='Логотип')
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added',)
        db_table = 'tournament'
        verbose_name = 'Соревнование'
        verbose_name_plural = 'Соревнования'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.logo:
            return 'http://127.0.0.1:8000' + self.logo.url


class TournamentRules(models.Model):
    min_members_in_team = models.IntegerField(verbose_name='Мин. кол-во участников в команде')
    max_members_in_team = models.IntegerField(verbose_name='Макс. кол-во участников в команде')
    date_start = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата начала')
    date_end = models.DateField(auto_now=False, auto_now_add=False, verbose_name='Дата окончания')
    id_tournament = models.OneToOneField(Tournament, on_delete=models.CASCADE, verbose_name='Соревнование')

    class Meta:
        db_table = 'tournament_rules'
        verbose_name = 'Правило'
        verbose_name_plural = 'Правила'


class TournamentAssessment(models.Model):
    name_criterion = models.CharField(max_length=50)
    result = models.IntegerField()
    id_tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    id_team = models.ForeignKey('Team', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tournament_assessment'
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='uploads/team_logo', blank=True, null=True, verbose_name='Логотип')
    id_tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    class Meta:
        db_table = 'team'
        verbose_name = 'Команду'
        verbose_name_plural = 'Команды'
    