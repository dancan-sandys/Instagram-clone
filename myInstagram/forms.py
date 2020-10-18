from .models import Photo

class NewPhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ['user','comments', 'likes','date']