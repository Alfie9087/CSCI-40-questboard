from django.db import models

from django.urls import reverse


class QuestboardModel(models.Model):
    boardName = models.CharField(
        max_length=100, null=True, verbose_name="Board Name")
    boardDescription = models.CharField(
        max_length=100, null=True, verbose_name="Board Description")
    numStars = models.IntegerField(default=0, verbose_name="Number of Stars")

    def __str__(self):
        return "{}".format(self.boardName)


class QuestModel(models.Model):
    boardOrigin = models.ForeignKey(
        QuestboardModel, on_delete=models.CASCADE,
        verbose_name="Board Name", null=True)
    questName = models.CharField(
        max_length=100, null=True, verbose_name="Quest Name")
    questDescription = models.CharField(
        max_length=100, null=True, verbose_name="Quest Description")
    numStars = models.IntegerField(default=0, verbose_name="Number of Stars")
    forAll = models.BooleanField(default=True, verbose_name="For all students")
    student1 = models.CharField(
        max_length=99, null=True,
        blank="True", default="", verbose_name="student 1",)
    student2 = models.CharField(
        max_length=99, null=True,
        blank="True", default="", verbose_name="student 2",)
    student3 = models.CharField(
        max_length=99, null=True,
        blank="True", default="", verbose_name="student 3",)

    def __str__(self):
        return "{}".format(self.questName)
