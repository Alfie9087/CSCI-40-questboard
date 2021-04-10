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


# def QuestPage(request, pk):
#     quests = QuestModel.objects.all()
#     questboard = QuestboardModel.objects.get(id=pk)
#     print(questboard)
#     form = QuestForm(request.POST)
#     if request.method == "POST":
#         form = QuestForm(request.POST)
#         if form.is_valid():
#             oldform = form
#             oldform.save()
#             form = QuestModel(
#                 boardOrigin=QuestboardModel.objects.get(boardName=questboard.boardName),
#                 questName = QuestModel.objects.get(questName=oldform.questName),
#             )
#             form.save()
#         return redirect("/questboard")
#     return render(request, "questspage.html", {"quests": quests, "questboard":questboard, "form": form})

def QuestPage(request, pk):
    questboard = QuestboardModel.objects.get(id=pk)
    quests = QuestModel.objects.all()
    return render(request, "questspage.html", {"quests": quests, "questboard":questboard})


# def quest_create(request, pk):
#     origin = QuestboardModel.objects.get(id=pk)
#     addForm = AddQuestForm(request.POST or None)
#     if addForm.is_valid():
#         quest = addForm.save(commit=False) 
#         quest.origin_questboard = origin 
#         quest.save()
#         return redirect('questboard_detail', pk)
    

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
    form = DibsForm1(instance=quests)
    
    if request.method == "POST":
        form = DibsForm1(request.POST, instance=quests)
        if form.is_valid():
            form.save()
            return redirect("/questboard")
    return render(request,"dibs.html", {"form": form})


def secondslot(request, pk):
    quests = QuestModel.objects.get(id=pk)
    form = DibsForm2(instance=quests)
    
    if request.method == "POST":
        form = DibsForm2(request.POST, instance=quests)
        if form.is_valid():
           form.save()
           return redirect("/questboard")
    return render(request,"dibs.html", {"form": form})


def thirdslot(request, pk):
    quests = QuestModel.objects.get(id=pk)
    form = DibsForm3(instance=quests)
    
    if request.method == "POST":
        form = DibsForm3(request.POST, instance=quests)
        if form.is_valid():
            form.save()
            return redirect("/questboard")
    return render(request,"dibs.html", {"form": form})

# def Dibs(request, pk):
#     quests = QuestModel.objects.get(id=pk)
#     student1 = DibsForm1(instance=quests)
#     form2 = DibsForm2(instance=quests)
#     form3 = DibsForm3(instance=quests)
    
#     if request.method == 'POST':
#         print("a")
#         if "first" in request.POST:
#             student1 = DibsForm1(request.POST, instance=profile)
#             if student1.is_valid():
#                 student1.save()

#         if "form2" in request.POST:
#             form2 = DibsForm2(request.POST, instance=profile)
#             if form2.is_valid():
#                 form2.save()

#         if "form3" in request.POST:
#             form3 = DibsForm3(request.POST, request.FILES, instance=profile)
#             if form3.is_valid():
#                 form3.save()

#     return render(request, "dibs.html", {"student1": student1, "form2": form2, "form3": form3, "quests": quests})

#redirect(request.get_full_path())