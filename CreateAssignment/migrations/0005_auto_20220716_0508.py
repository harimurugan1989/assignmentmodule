# Generated by Django 3.2.8 on 2022-07-16 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0004_assignquestion_qno'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignquestion',
            name='des1',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='assignquestion',
            name='des2',
            field=models.TextField(blank=True),
        ),
    ]
