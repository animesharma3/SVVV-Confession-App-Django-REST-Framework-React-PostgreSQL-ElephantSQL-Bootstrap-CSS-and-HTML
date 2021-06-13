from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import serializers
from . import models

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/confessions/',
        'Detail View': '/confessions/:id',
        'Create': '/confession/create',
        'Update': '/confession/edit/:id',
        'Delete': '/confession/delete/:id',
    }

    return Response(api_urls)

@api_view(['GET'])
def confessionList(request):
    confessions = models.Confession.objects.all().order_by('-created_at')
    serializer = serializers.ConfessionSerializer(confessions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def confessionDetail(request, pk):
    confessions = models.Confession.objects.get(id=pk)
    serializer = serializers.ConfessionSerializer(confessions, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def confessionCreate(request):
    serializer = serializers.ConfessionSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def confessionEdit(request, pk):
    confession = models.Confession.objects.get(id=pk)
    serializer = serializers.ConfessionSerializer(instance=confession, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def confessionDelete(request, pk):
    confession = models.Confession.objects.get(id=pk)
    confession.delete()

    return Response("Confession Successfully delete")