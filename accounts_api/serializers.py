from rest_framework import serializers
from django.contrib.auth.models import User
from . import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = '__all__'

class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'