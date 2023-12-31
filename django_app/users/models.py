from django.db import models
from django.contrib.auth.models import  User
from PIL import Image

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/1.jpg')



    def __str__(self):

        return f"{self.user.username} Profile"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            out_size = (300,300)
            img.resize(out_size)
            img.save(self.image.path)