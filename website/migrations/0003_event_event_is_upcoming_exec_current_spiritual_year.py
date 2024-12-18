# Generated by Django 5.1.4 on 2024-12-12 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_ministry_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_is_upcoming',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='exec',
            name='current_spiritual_year',
            field=models.CharField(default='2024/2025', max_length=50),
        ),
    ]
