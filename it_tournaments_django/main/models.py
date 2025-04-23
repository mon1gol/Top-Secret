from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


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
            return 'https://apitournaments.it-tournaments.ru/' + self.logo.url
        return ''


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


class Criterion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название критерия')
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    max_score = models.PositiveIntegerField(verbose_name='Максимальный балл')

    class Meta:
        db_table = 'criterion'
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'

    def __str__(self):
        return self.name
    

class TournamentCriterion(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='criteria', on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, related_name='tournaments', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tournament_criterion'
        verbose_name = 'Критерий соревнования'
        verbose_name_plural = 'Критерии соревнований'

    def __str__(self):
        return f"{self.tournament.name} - {self.criterion.name}"


class TeamAssessment(models.Model):
    team = models.ForeignKey('Team', related_name='assessments', on_delete=models.CASCADE)
    tournament = models.ForeignKey(Tournament, related_name='assessments', on_delete=models.CASCADE)
    criterion = models.ForeignKey(Criterion, related_name='assessments', on_delete=models.CASCADE)
    score = models.PositiveIntegerField(verbose_name='Оценка')

    class Meta:
        db_table = 'team_assessment'
        verbose_name = 'Оценка команды'
        verbose_name_plural = 'Оценки команд'

    def __str__(self):
        return f"{self.team.name} - {self.criterion.name}: {self.score}"


class Team(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='uploads/team_logo', blank=True, null=True, verbose_name='Логотип')
    id_tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    class Meta:
        db_table = 'team'
        ordering = ('name',)
        verbose_name = 'Команду'
        verbose_name_plural = 'Команды'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            unique_slug = base_slug
            counter = 1

            while Team.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = unique_slug
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name} - {self.id_tournament.name}"

    def get_image(self):
        if self.logo:
            return 'https://apitournaments.it-tournaments.ru/' + self.logo.url
        return ''   
    
    def get_absolute_url(self):
        return f'/{self.id}/'
    
class LinkToTeamMember(models.Model):
    user = models.ForeignKey(User, related_name='team_memberships', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='members', on_delete=models.CASCADE)

    class Meta():
        db_table = 'link_to_team_member'
        verbose_name = 'Связь участника с командой'
        verbose_name_plural = 'Связи участников с командой'

    def __str__(self):
        return f"{self.user.username} in {self.team.name}"
    
class TeamProject(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='tournament_projects', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='projects', on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    file_name = models.FileField(upload_to='uploads/projects', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta():
        db_table = 'team_projects'
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f"{self.tournament.name} - {self.team.name} - {self.date_added}"
    
    def get_file_project(self):
        if self.file_name:
            return 'https://apitournaments.it-tournaments.ru/' + self.file_name.url
        return ''
