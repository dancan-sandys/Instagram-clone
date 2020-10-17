from django.db import models

# Create your models here.


#classes

class Profile(models.Model):
    name = models.Charfield(max_length(60))
    proile_photo = models.Imagefield(upload_to = 'instagram/')
    bio = models.Charfield(max_length(120))
    email = models.Charfield(max_length(30))
    username = models.Charfield(max_length(30))
    password = models.Charfield(max_length(30))

    def saveprofile(self):
        self.save()

    def deleteprofile(self):
        self.delete()

    def updateprofile(self, bio):
        self.bio = bio if bio else self.bio
        self.save()


class Comments(models.Model):
    commenter = models.Charfield(max_length(30))
    comment = models.Textfield(max_length(500))


class Photo(models.Model):

    name = models.Charfield(max_length(30))
    photo_url = models.Imagefield(upload_to = 'instagram/')
    user = models.ForeignKey(Profile, on_delete = models.CASCADE,)
    captions = models.Charfield(max_length(160))
    likes = models.Integerfield()
    comments = models.ForeignKey(Comments, on_delete = models.CASCADE,)

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

