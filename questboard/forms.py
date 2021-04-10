from django import forms

from django.utils.safestring import mark_safe

from .models import (
    QuestboardModel, QuestModel,
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

class DibsForm1(forms.ModelForm):
    class Meta:
        model = QuestModel
        fields = [
            "student1",
        ]
class DibsForm2(forms.ModelForm):
    class Meta:
        model = QuestModel
        fields = [
             "student2",
        ]
class DibsForm3(forms.ModelForm):
    class Meta:
        model = QuestModel
        fields = [
             "student3",
        ]