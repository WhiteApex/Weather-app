# Generated by Django 4.2.14 on 2024-07-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wheather', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchhistory',
            name='login',
            field=models.CharField(blank=True, max_length=30, unique=True),
        ),
    ]
