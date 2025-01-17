# Generated by Django 5.1.4 on 2025-01-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_home_county_customuser_homecounty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(default='full name', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='homeCounty',
            field=models.CharField(default='county', max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='0712345678', max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='registrationNumber',
            field=models.CharField(default='S13/12345/20', max_length=20, unique=True),
        ),
    ]
