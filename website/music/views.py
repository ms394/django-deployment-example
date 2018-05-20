from django.shortcuts import render
from django.http import HttpResponse
from music.models import Album,Song

# Create your views here.
def home(request):
    return render(request, 'home.html', context=None)
    
def index(request):
    all_albums = Album.objects.all()
    album_dict = {'albumrecords':all_albums}
    return render(request,'index.html',context=album_dict)


def detail(request,album_title):
    return HttpResponse("<p>hello "+ album_title+"</p>")
