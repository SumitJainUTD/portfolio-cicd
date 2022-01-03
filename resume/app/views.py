from django.shortcuts import render
from .models import Tile
from .models import Skill


# Create your views here.
def home(request):
    skills = Skill.objects
    return render(request, 'app/sumit.html', {"skills": skills})


def jobs(request):
    tiles = Tile.objects
    return render(request, 'app/jobs.html', {"tiles": tiles})

