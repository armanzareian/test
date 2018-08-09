from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     First_name=models.CharField(max_length=264)
#     Last_name=models.CharField(max_length=264)
#     Email=models.EmailField()
#
#     def __str__(self):
#         return self.First_name+" "+self.Last_name+" "+self.Email
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    profile_pic=models.ImageField(upload_to="profile_pics",blank=True)

    def __str__(self):
        return self.user.username
