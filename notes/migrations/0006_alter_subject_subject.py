# Generated by Django 3.2.7 on 2021-11-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_alter_subject_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject',
            field=models.CharField(default='Others', max_length=50, unique=True),
        ),
    ]
