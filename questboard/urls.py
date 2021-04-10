from django.urls import path
from .views import (
    index, QuestboardPage,
    QuestboardCreate,
     QuestboardUpdate,
     QuestPage,
     QuestUpdate,
     QuestCreate, firstslot, secondslot,
     thirdslot)

urlpatterns = [
    path('', index, name='index'),
    path('questboard', QuestboardPage, name='questboard'),
    path("questboard_create", QuestboardCreate, name="questboard_create"),
    path("questboard_update/<int:pk>", QuestboardUpdate, name="questboard_update"),
    path("questpage/<int:pk>", QuestPage, name="questpage"),
    path("quest_create/<int:pk>", QuestCreate, name="quest_create"),
    path("quest_update/<int:pk>", QuestUpdate, name="quest_update"),
    path("slot1/<int:pk>", firstslot, name="slot1"),
    path("slot2/<int:pk>", secondslot, name="slot2"),
    path("slot3/<int:pk>", thirdslot, name="slot3"),
]