# Generated by Django 3.2.7 on 2022-02-28 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word', '0002_vocab_meaning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vocab',
            name='word',
            field=models.CharField(max_length=1000),
        ),
    ]
