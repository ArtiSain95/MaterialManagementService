# materials/serializers.py
from rest_framework import serializers
from .models import Material

class MaterialSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Material model.

    Attributes:
        model (class): The Django model associated with the serializer.
        fields (list): The fields to include in the serialized output.

        A MaterialSerializer instance can be used to convert a Material object
        into a JSON representation with the specified fields.
    """
    class Meta:
        model = Material
        fields = ['id', 'formula', 'density']
