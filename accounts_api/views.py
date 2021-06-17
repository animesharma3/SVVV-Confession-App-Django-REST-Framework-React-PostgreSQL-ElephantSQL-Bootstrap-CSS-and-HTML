from accounts_api import serializers
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from . import models
from . import serializers

@api_view(['GET'])
def userProfileList(request):
    profiles = models.UserProfile.objects.all()
    serializer = serializers.UserProfileSerializer(profiles, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userProfileDetail(request, pk):
    profiles = models.UserProfile.objects.get(id=pk)
    serializer = serializers.UserProfileSerializer(profiles, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def AccountDetail(request, pk):
    accounts = User.objects.get(id=pk)
    serializer = serializers.AccountsSerializer(accounts, many=False)
    return Response(serializer.data)

@api_view(['GET'])
def currentUser(request):
    user = request.user
    return Response({
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'bio': user.profile.bio,
        'profile_pic': user.profile.profile_pic,
        'profile_pic': user.profile.phone_no,
        'facebook_url': user.profile.facebook_url,
        'instagram_url': user.profile.instagram_url,
        'user_id': user.id,
        'profile_id': user.profile.id,
    })