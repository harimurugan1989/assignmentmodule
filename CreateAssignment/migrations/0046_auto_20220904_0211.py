# Generated by Django 3.2.8 on 2022-09-04 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CreateAssignment', '0045_alter_flipcustomize_fcpanel'),
    ]

    operations = [
        migrations.AddField(
            model_name='flipcustomize',
            name='fweb',
            field=models.URLField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='flipcustomize',
            name='fskin',
            field=models.CharField(default='#030000', max_length=2),
        ),
    ]
