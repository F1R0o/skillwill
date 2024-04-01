from django.db import models
from PIL import Image
# Create your models here.
class Users(models.Model):
    saxeli = models.CharField(max_length=20)
    gvari = models.CharField(max_length=20)
    asaki = models.IntegerField()
    email = models.EmailField(unique=True)
    profile_picture = models.ImageField(upload_to="profile_pictures/", null=True, blank=True)

    def __str__(self):
        return f"{self.saxeli}| {self.gvari}"

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.profile_picture:
            img = Image.open(self.profile_picture.path)
            if img.height > 500 or img.width > 500:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)