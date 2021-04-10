from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import QuestboardModel, QuestModel

from .forms import QuestboardForm

from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.views.generic.detail import DetailView


def index(request):
    return redirect("/questboard")
    

def QuestboardPage(request):
    questboards = QuestboardModel.objects.all()
    return render(request, 'questboard.html', {"questboards":questboards})


def QuestboardCreate(request):
    form = QuestboardForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect("/questboard")
    return render(request, "questboard_edit.html", {"form": form})


def QuestboardUpdate(request, pk):
    questboard = QuestboardModel.objects.get(id=pk)
    form = QuestboardForm(instance=questboard)

    if request.method == "POST":
        form = QuestboardForm(request.POST, instance=questboard)
        if form.is_valid():
            form.save()
            return redirect("/questboard")
    return render(request, "questboard_edit.html", {"form": form})

def QuestPage(request, pk):
    return render(request, "quest.html")
