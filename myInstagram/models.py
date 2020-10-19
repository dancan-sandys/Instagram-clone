from django.db import models
from django.contrib.auth.models import User


# Create your models here.


#classes

class Profile(models.Model):
    name = models.CharField(max_length = 60)
    profile_photo = models.CharField(max_length=20)
    bio = models.CharField(max_length =130)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    def updateprofile(self, bio):
        self.bio = bio if bio else self.bio
        self.save()

    

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length = 500)

    def savecomments(self):
        self.save()

    def deletecomments(self):
        self.delete()

    def updatecomments(self, comment):
        self.comment = comment if comment else self.comment
        self.save()

class Photo(models.Model):

    name = models.CharField(max_length =30)
    photo_url = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    captions = models.CharField(max_length =160)
    likes = models.IntegerField()
    comments = models.ForeignKey(Comments, on_delete = models.CASCADE,)


    def savephoto(self):
        self.save()

    def deletephoto(self):
        self.delete()

    def updatephoto(self, photo):
        self.photo_url = photo if photo else self.photo_url
        self.save()

    def likephoto(self):
        self.likes = likes + 1
        self.save()

