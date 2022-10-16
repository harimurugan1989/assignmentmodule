# Generated by Django 3.2.8 on 2022-08-12 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CreateAssignment', '0028_auto_20220812_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='flipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=12)),
                ('fname', models.CharField(max_length=40)),
                ('upload', models.FileField(upload_to='flipupload')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
