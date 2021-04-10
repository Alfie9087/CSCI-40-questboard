from django.urls import path
from .views import (
    index, QuestboardPage,
    QuestboardCreate,
     QuestboardUpdate,
     QuestPage, QuestCreate)

urlpatterns = [
    path('', index, name='index'),
    path('questboard', QuestboardPage, name='questboard'),
    path("questboard_create", QuestboardCreate, name="questboard_create"),
    path("questboard_update/<int:pk>", QuestboardUpdate, name="questboard_update"),
    path("questpage/<int:pk>", QuestPage, name="questpage"),
    path("quest_create/", QuestCreate, name="quest_create"),
]