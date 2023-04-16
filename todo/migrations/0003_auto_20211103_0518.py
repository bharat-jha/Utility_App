# Generated by Django 3.2.7 on 2021-11-03 05:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0002_todolist_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='id',
        ),
        migrations.AlterField(
            model_name='todolist',
            name='Owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
