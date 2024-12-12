from django.db import models

# Create your models here.
POSITIONS = [
    ('Chairperson', 'Chairperson'),
    ('Vice Chairperson', 'Vice Chairperson'),
    ('Secretary', 'Secretary'),
    ('Treasurer', 'Treasurer'),
    ('Vice Secretary', 'Vice Secretary'),
    ('Organizing Secretary', 'Organizing Secretary'),
    ('Librarian', 'Librarian'),
    ('Missions Coordinator', 'Missions Coordinator'),
    ('Bible Study Coordinator', 'Bible Study Coordinator'),
    ('Technical Coordinator', 'Technical Coordinator'),
    ('Music Director', 'Music Director'),
    ('Prayer Secretary', 'Prayer Secretary'),
]

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='media/events')
    event_date = models.DateField()
    event_description = models.TextField()
    event_venue = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.event_name}- {self.event_date}"

class Testimony(models.Model):
    testimony_giver = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/testimonies')
    position = models.CharField(max_length=100)
    testimony = models.TextField()

    def __str__(self):
        return f"{self.testimony_giver} testimony."


class Exec(models.Model):
    spiritual_year = models.CharField(max_length=50)
    group_image = models.ImageField(upload_to='media/execs', null=True, blank=True)

    def __str__(self):
        return f"{self.spiritual_year}"

class Leader(models.Model):
    leader_name = models.CharField(max_length=150)
    leader_image = models.ImageField(upload_to='media/leaders')
    leader_position = models.CharField(max_length=150, choices=POSITIONS)
    leader_description = models.TextField()
    leader_contact = models.CharField(max_length=50)
    exec_year = models.ForeignKey(Exec, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.leader_position} - {self.exec_year}"

class Ministry(models.Model):
    ministry_name = models.CharField(max_length=100)
    ministry_image = models.ImageField(upload_to='media/ministries')
    ministry_description = models.TextField()
    ministry_chair = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "ministries"

    def __str__(self):
        return f"{self.ministry_name}"

class Eteam(models.Model):
    team_name =  models.CharField(max_length=100)
    team_image = models.ImageField(upload_to='media/ministries')
    team_description = models.TextField()
    team_chair = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.team_name}"
    
