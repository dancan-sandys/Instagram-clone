from django.db import models

# Create your models here.


#classes

class Profile(models.Model):
    name = models.Charfield(max_length(60))
    bio = models.Charfield(max_length(120))
    email = models.Charfield(max_length(30))
    username = models.Charfield(max_length(30))
    password = models.Charfield(max_length(30))

class Photo(models.Model):

    name = models.Charfield(max_length(30))
    photo_url = models.Imagefield(upload_to = 'instagram/')
    user = models.ForeignKey(Profile, on_delete = models.CASCADE,)


