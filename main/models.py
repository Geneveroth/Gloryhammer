from django.db import models

class Angus(models.Model):
    angus_hp = models.IntegerField()
    angus_hit = models.IntegerField()
    angus_dmg = models.IntegerField()
    inventory = {}