# Generated by Django 3.2.8 on 2022-07-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0022_alter_questiondata_rmax2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questiondata',
            name='rmax2',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='questiondata',
            name='rmin3',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
