# Generated by Django 3.2.7 on 2021-11-08 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20211108_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='pic',
            field=models.ImageField(upload_to='notes/images/'),
        ),
    ]