from django.shortcuts import render, request
from models import Photo,Profile,Comments

# Create your views here.

#user profile
def profile(request, id):
    user = profile.Profile.objects.get(id = id)

    return render(request, 'profile.html', {"user":user})

def photos(request):

    Photos = Photo.objects.all()

    return render(request, 'photos.html', {"photos":photos})

def image(request, id):

    image = Photo.objects.get(id =id)

    return render(request, 'image.html', {"photo": image})