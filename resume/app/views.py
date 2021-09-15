from django.shortcuts import render
from .models import Tile


# Create your views here.
def home(request):
    tiles = Tile.objects
    return render(request, 'app/sumit.html', {"tiles": tiles})

def jobs(request):
    tiles = Tile.objects
    return render(request, 'app/jobs.html', {"tiles": tiles})
