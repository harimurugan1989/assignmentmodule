# Generated by Django 4.1 on 2022-10-04 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='qno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CreateAssignment.question'),
        ),
    ]
