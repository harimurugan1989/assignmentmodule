# Generated by Django 3.2.8 on 2022-07-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0021_alter_questiondata_rmin2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiondata',
            name='rmax2',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
