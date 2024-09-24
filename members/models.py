from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField



# Create your models here.

# Create A User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True, region='GB')
    date_modified = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default_profile_image.png")
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return f"{self.user.username},{self.name},{self.phone_number}"



'''
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(User, auto_now=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to="images/", default="images/default_profile_image.png")
    profile_bio = models.CharField(null=True, blank=True, max_length=500)
    facebook_link = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return self.user.username
 '''  
# Create Profile When New User Signs Up
# @receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
            

post_save.connect(create_profile, sender=User)
