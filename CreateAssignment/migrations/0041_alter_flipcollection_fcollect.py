# Generated by Django 3.2.8 on 2022-08-14 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0040_flipcollection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flipcollection',
            name='fcollect',
            field=models.BooleanField(default=False),
        ),
    ]
