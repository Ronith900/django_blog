from django.db import models
from blog.models import AbstractModel
from django.contrib.auth.models import User
from PIL import Image


class Profile(AbstractModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics')
    country = models.CharField(max_length=250,blank=True,null=True,default=None)
    dob = models.CharField(max_length=250, blank=True, null=True, default=None)
    occupation = models.CharField(max_length=250, blank=True, null=True, default=None)
    bio = models.TextField(blank=True,null=True,default=None)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)