from django.urls import path
from .views import (
    index, QuestboardPage,
    QuestboardCreate,
     QuestboardUpdate,
     QuestPage,
     QuestUpdate,
     QuestCreate)

urlpatterns = [
    path('', index, name='index'),
    path('questboard', QuestboardPage, name='questboard'),
    path("questboard_create", QuestboardCreate, name="questboard_create"),
    path("questboard_update/<int:pk>", QuestboardUpdate, name="questboard_update"),
    path("questpage/<int:pk>", QuestPage, name="questpage"),
    path("quest_create/<int:pk>", QuestCreate, name="quest_create"),
    path("quest_update/<int:pk>", QuestUpdate, name="quest_update"),
]