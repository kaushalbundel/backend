from rest_framework import serializers
from .models import Todo


class TodoSerializers(
    serializers.ModelSerializer
):  # I am guessing there can be different ways to create serializers, using models (Model.Serializer is just one of the ways to do so)
    class Meta:
        model = Todo
        fields = [
            "id",
            "title",
            "body",
        ]
