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
def AccountDetail(request, pk):
    accounts = User.objects.get(id=pk)
    serializer = serializers.AccountsSerializer(accounts, many=False)
    return Response(serializer.data)