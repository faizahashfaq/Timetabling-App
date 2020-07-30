# Generated by Django 3.0.8 on 2020-07-30 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Activity_Scheduler', '0003_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='dwk',
            field=models.SmallIntegerField(default=7),
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TimeSlot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Activity_Scheduler.TimeSlot')),
            ],
        ),
    ]