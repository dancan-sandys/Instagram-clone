from django.db import models
from django.contrib.auth.models import User


# Create your models here.


#classes

class Profile(models.Model):
    name = models.CharField(max_length = 60)
    bio = models.TextField(max_length =130)
    profile_photo = models.ImageField(upload_to = 'profile/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    def updateprofile(self, bio):
        self.bio = bio if bio else self.bio
        self.save()

    
class Photo(models.Model):

    name = models.CharField(max_length =30)
    photo_url = models.ImageField(upload_to= 'photos/')
    user = models.ForeignKey(User, on_delete = models.CASCADE,)
    captions = models.CharField(max_length =160)
    likes = models.IntegerField()
    


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


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length = 500)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)

    def savecomments(self):
        self.save()

    def deletecomments(self):
        self.delete()

    def updatecomments(self, comment):
        self.comment = comment if comment else self.comment
        self.save()
