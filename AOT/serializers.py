from rest_framework import serializers
from .models import AOT

class AOTSerializer(serializers.ModelSerializer):
    class Meta:
        model = AOT
        fields = '__all__'
