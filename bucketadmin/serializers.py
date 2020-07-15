from .models import Funpost
from rest_framework import serializers

class FunpostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Funpost
        fields = '__all__'
        depth = 1