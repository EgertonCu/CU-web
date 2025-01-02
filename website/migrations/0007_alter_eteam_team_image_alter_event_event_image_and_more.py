# Generated by Django 5.1.4 on 2024-12-21 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eteam',
            name='team_image',
            field=models.ImageField(upload_to='ministries'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_image',
            field=models.ImageField(upload_to='events'),
        ),
        migrations.AlterField(
            model_name='exec',
            name='group_image',
            field=models.ImageField(blank=True, null=True, upload_to='execs'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='gallery'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='leader_image',
            field=models.ImageField(upload_to='leaders'),
        ),
        migrations.AlterField(
            model_name='ministry',
            name='ministry_image',
            field=models.ImageField(upload_to='ministries'),
        ),
        migrations.AlterField(
            model_name='testimony',
            name='image',
            field=models.ImageField(upload_to='testimonies'),
        ),
    ]
