from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

url_regex = '^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$'
url_validator = RegexValidator(url_regex, "Invalid URL")

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to = 'images/profile/')
    phone_no = models.CharField(max_length=20, blank=True, null=True)
    instagram_url = models.CharField(max_length=300, validators=[url_validator], blank=True, null=True)
    facebook_url = models.CharField(max_length=300, validators=[url_validator], blank=True, null=True)

    def __str__(self):
        return str(self.user)