# Generated by Django 3.2.8 on 2022-08-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0027_st_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='createlink',
            name='responses',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createlink',
            name='first_sub_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createlink',
            name='no_of_submissions',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='createlink',
            name='perc_penalty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='createlink',
            name='result_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createlink',
            name='second_sub_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='createlink',
            name='start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
