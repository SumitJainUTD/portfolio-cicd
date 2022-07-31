from django.db import models


# Create your models here.
class Tile(models.Model):
    image = models.ImageField(upload_to='images/')
    display_id = models.IntegerField(blank=True, default=1)
    title = models.CharField(max_length=50, blank=True)
    company = models.CharField(max_length=50, blank=True)
    detail = models.TextField(max_length=1000, blank=True)

    class Meta:
        ordering = ('display_id',)


class Skill(models.Model):
    name = models.CharField(max_length=50, blank=True)
