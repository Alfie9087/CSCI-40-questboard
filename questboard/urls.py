from django.urls import path
from .views import (
    index, QuestboardPage,
    QuestboardCreate, QuestboardUpdate)

urlpatterns = [
    path('', index, name='index'),
    path('questboard', QuestboardPage, name='questboard'),
    path("questboard_create", QuestboardCreate, name="questboard_create"),
    path("questboard_update/<str:pk>", QuestboardUpdate, name="questboard_update"),
    path("questpage/<str:pk>", QuestboardUpdate, name="questpage"),
]