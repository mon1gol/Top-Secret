from django.db import models


class Hackathon(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='hackathon_images', blank=True, null=True, height_field=None, width_field=None, max_length=None)

    class Meta:
        db_table = 'hackathon'


class HackathonRules(models.Model):
    min_members_in_team = models.IntegerField()
    max_members_in_team = models.IntegerField()
    date_start = models.DateField(auto_now=False, auto_now_add=False)
    date_end = models.DateField(auto_now=False, auto_now_add=False)
    id_hackathon = models.OneToOneField(Hackathon, on_delete=models.CASCADE)

    class Meta:
        db_table = 'hackathon_rules'


class HackathonAssessment(models.Model):
    name_criterion = models.CharField(max_length=50)
    result = models.IntegerField()
    id_hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    id_team = models.ForeignKey('Team', on_delete=models.CASCADE)

    class Meta:
        db_table = 'hackathon_assessment'


class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='team_images', blank=True, null=True, height_field=None, width_field=None, max_length=None)
    id_hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)

    class Meta:
        db_table = 'team'
    