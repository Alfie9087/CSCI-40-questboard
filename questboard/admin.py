from django.contrib import admin

from .models import (
    QuestboardModel,
    QuestModel
    )

class QuestboardAdmin(admin.ModelAdmin):
    model = QuestboardModel


class QuestAdmin(admin.ModelAdmin):
    model = QuestModel

admin.site.register(QuestboardModel)
admin.site.register(QuestModel)