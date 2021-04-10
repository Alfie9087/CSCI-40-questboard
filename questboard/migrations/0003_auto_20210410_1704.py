# Generated by Django 3.1.7 on 2021-04-10 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questboard', '0002_questmodel_questdescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questmodel',
            name='boardOrigin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='questboard.questboardmodel', verbose_name='Board Name'),
        ),
    ]