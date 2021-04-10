from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import QuestboardModel, QuestModel

from .forms import QuestboardForm, QuestForm, DibsForm1, DibsForm2, DibsForm3

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
    if request.method == "POST":
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
    questboard = QuestboardModel.objects.get(id=pk)
    quests = QuestModel.objects.all()
    return render(request, "questspage.html", {"quests": quests, "questboard":questboard})
    

def QuestCreate(request, pk):
    originname = QuestboardModel.objects.get(id=pk)
    form = QuestForm(request.POST or None)
    if form.is_valid():
        quest = form.save(commit=False)
        quest.boardOrigin = originname
        quest.save()
        return redirect("questpage", pk)
    return render(request, "quest_edit.html", {"form": form, "boards":originname})


def QuestUpdate(request, pk):
    quests = QuestModel.objects.get(id=pk)
    form = QuestForm(instance=quests)

    if request.method == "POST":
        form = QuestForm(request.POST, instance=quests)
        if form.is_valid():
            form.save()
            return redirect("questpage", pk)
    return render(request, "quest_edit.html", {"form": form})


def firstslot(request, pk):
    quests = QuestModel.objects.get(id=pk)
    origin = quests.boardOrigin
    form = DibsForm1(instance=quests)
    if request.method == "POST":
        form = DibsForm1(request.POST, instance=quests)
        if form.is_valid():
            form.save()
            return redirect("questpage", origin.pk)
    return render(request,"dibs.html", {"form": form})


def secondslot(request, pk):
    quests = QuestModel.objects.get(id=pk)
    origin = quests.boardOrigin
    form = DibsForm2(instance=quests)
    
    if request.method == "POST":
        form = DibsForm2(request.POST, instance=quests)
        if form.is_valid():
           form.save()
           return redirect("questpage", origin.pk)
    return render(request,"dibs.html", {"form": form})


def thirdslot(request, pk):
    quests = QuestModel.objects.get(id=pk)
    origin = quests.boardOrigin
    form = DibsForm3(instance=quests)
    
    if request.method == "POST":
        form = DibsForm3(request.POST, instance=quests)
        if form.is_valid():
            form.save()
            return redirect("questpage", origin.pk)
    return render(request,"dibs.html", {"form": form})
