from django.db.models import fields
from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        # fields = "__all__" 
        fields = 'id name'.split()
        # fields = ["id", 'name'] Второй способ
        

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"

