from rest_framework import serializers

from . import models

class ConfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Confession
        fields = '__all__'