# Generated by Django 3.2.7 on 2021-11-25 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=100)),
                ('Subject', models.CharField(max_length=180)),
                ('Message', models.TextField()),
            ],
        ),
    ]
