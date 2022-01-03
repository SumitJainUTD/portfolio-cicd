from django.contrib import admin

# Register your models here.
from .models import Tile
from .models import Skill

admin.site.register(Tile)
admin.site.register(Skill)