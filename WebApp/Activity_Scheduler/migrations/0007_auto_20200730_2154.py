# Generated by Django 3.0.8 on 2020-07-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Activity_Scheduler', '0006_auto_20200730_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='Class',
            field=models.ManyToManyField(default=None, to='Activity_Scheduler.Class'),
        ),
    ]