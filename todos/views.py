from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializers


class ListToDo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers


class DetailToDo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers
