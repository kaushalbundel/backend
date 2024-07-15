from django.urls import path, include
from .views import ListToDo, DetailToDo

urlpatterns = [
    path("", ListToDo.as_view()),
    path(
        "<int:pk>/", DetailToDo.as_view()
    ),  # in this case we have not used the name argument as this url will not be used in creating the template
]
