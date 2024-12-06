from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    login = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254,)
    password = models.CharField(max_length=255)
    id_team = models.OneToOneField('main.Team', on_delete=models.CASCADE, default='Null', blank=True)

    class Meta:
        db_table = 'user'


class Role(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'role'


class RoleUser(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_role = models.ForeignKey(Role, on_delete=models.CASCADE, default=0)

    class Meta:
        db_table = 'role_user'
