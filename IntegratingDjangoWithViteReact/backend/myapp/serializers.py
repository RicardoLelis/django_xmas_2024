from rest_framework import serializers
from .models import Language

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ['id', 'name']

class LanguageDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'