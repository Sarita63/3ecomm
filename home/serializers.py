from rest_framework import  serializers, viewsets
from .models import *
# Serializers define the API representation.
class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"
