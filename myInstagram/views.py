from django.shortcuts import render
from .models import Photo,Profile,Comments
from django.contrib.auth.decorators import login_required
from .forms import NewPhotoForm, UpdateProfile, Comment

# Create your views here.

#user profile
def profile(request, id):
    user = Profile.objects.get(id = id)

    return render(request, 'profile.html', {"user":user})

@login_required(login_url= '/accounts/login/')
def photos(request):

    Photos = Photo.objects.all()

    return render(request, 'photos.html', {"photos":Photos})

def image(request, id):

    image = Photo.objects.get(id =id)

    return render(request, 'image.html', {"photo": image})



def search(request):

    return render(request, 'search.html')

def addphotos(request):
    current_user = request.user 
    if request.method == 'POST':
        form = NewPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.user = current_user

            photo.save()

        return redirect('photos')

    else:
        form = NewPhotoForm()

        return render(request, 'post.html',{"form": form})


def profileupdate(request):
    current_user = request.user
    if request.method = 'POST':
        form = UpdateProfile(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect('photos')

    else:
        form = UpdateProfile()

        return render(request, 'updateprofile.html'{"form":form})

def new_comment(request):
    current_user = request.current_user
    if request.method = 'POST':
        form = Comment(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user

            comment.save()
        return redirect('photos')     

    else:
        form = Comment()       

        return render(request, 'comment.hmtl', {"form":form})