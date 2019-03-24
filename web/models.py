from django.db import models
from django.contrib.auth.forms import User
# Create your models here.


class My_User(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.BigIntegerField()
    # profile_user = models.ImageField(upload_to='profile_image', blank=True)

    def __str__(self):
        return '{}-{}'.format(self.user, self.username)

class Photo(models.Model):
   #x user = models.OneToOneField(User, on_delete=models.CASCADE)
   #xpyt user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=23)

    def __str__(self):
        return '{}'.format(self.name)