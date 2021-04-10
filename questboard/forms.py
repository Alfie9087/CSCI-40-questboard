from django import forms

from django.utils.safestring import mark_safe

from .models import (
    QuestboardModel, QuestModel
    )

class QuestboardForm(forms.ModelForm):
    class Meta:
        model = QuestboardModel
        fields = [
            "boardName",
            "boardDescription",
            "numStars",
        ]

class QuestForm(forms.ModelForm):
    class Meta:
        model = QuestModel
        fields = [
            "questName",
            "questDescription",
            "numStars",
            "forAll"
        ]