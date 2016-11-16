from rest_framework import serializers
from models import programms

class programmSerializer(serializers.ModelSerializer):
    class Meta:
        model = programms;
        fields = ('id','name','coast','description');