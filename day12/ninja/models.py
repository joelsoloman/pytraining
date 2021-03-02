from django.db import models

# Create your models here.

class Developer(models.Model):
    name = models.CharField(max_length = 50)
    experience = models.IntegerField()
    country = models.CharField(max_length = 50)

    def __repr__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length = 50)
    level = models.CharField(max_length = 50)
    developer = models.ForeignKey(Developer, on_delete =  models.CASCADE)

    def __repr__(self):
        return self.name + " " + self.level
    