from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#classes

class Profile(models.Model):
    name = models.CharField(max_length = 60)
    profile_photo = models.ImageField(upload_to = 'instagram/')
    bio = models.CharField(max_length =120)
    email = models.CharField(max_length  = 30)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length =30)

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    def updateprofile(self, bio):
        self.bio = bio if bio else self.bio
        self.save()


class Comments(models.Model):
    commenter = models.CharField(max_length = 30)
    comment = models.TextField(max_length = 500)


class Photo(models.Model):

    name = models.CharField(max_length =30)
    photo_url = models.ImageField(upload_to = 'instagram/')
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    captions = models.CharField(max_length =160)
    likes = models.IntegerField()
    comments = models.ForeignKey(Comments, on_delete = models.CASCADE,)
    date = models.DateTimeField(auto_now_add=True)

    def savephoto(self):
        self.save()

    def deletephoto(self):
        self.delete()

    def updatephoto(self, bio):
        self.bio = bio if bio else self.bio
        self.save()

    def likephoto(self):
        self.likes = likes + 1
        self.save()

