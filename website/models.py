from django.db import models

# Create your models here.
#Exec positions choices
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

#Image category choices
IMAGE_CATEGORIES = [
    ('event', 'event'),
    ('service', 'service'),
    ('fellowship', 'fellowship'),
    ('outdoors', 'outdoors'),
]

#This is the Events model--used on the homepage
class Event(models.Model):
    event_name = models.CharField(max_length=100)
    event_image = models.ImageField(upload_to='media/events')
    event_date = models.DateField()
    event_description = models.TextField()
    event_venue = models.CharField(max_length=100)
    event_is_upcoming = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.event_name}- {self.event_date}"

#This is the testimonies model -- also used on the homepage
class Testimony(models.Model):
    testimony_giver = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/testimonies')
    position = models.CharField(max_length=100)
    testimony = models.TextField()

    class Meta:
        verbose_name_plural = "Testimonies"

    def __str__(self):
        return f"{self.testimony_giver}'s testimony."

#This is the exec model. It has been used to keep track of the executive committees and maintain their records even after they hand over
class Exec(models.Model):
    spiritual_year = models.CharField(max_length=50)
    current_spiritual_year = models.CharField(max_length=50, default='2024/2025')
    group_image = models.ImageField(upload_to='media/execs', null=True, blank=True)

    def __str__(self):
        return f"{self.spiritual_year}"

#This is the leaders model, for adding the exec leaders in the admin panel
class Leader(models.Model):
    leader_name = models.CharField(max_length=150)
    leader_image = models.ImageField(upload_to='media/leaders')
    leader_position = models.CharField(max_length=150, choices=POSITIONS)
    leader_description = models.TextField()
    leader_contact = models.CharField(max_length=50)
    exec_year = models.ForeignKey(Exec, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.leader_position} - {self.exec_year}"

#This is the ministries model, for adding the ministries in the admin panel
class Ministry(models.Model):
    ministry_name = models.CharField(max_length=100)
    ministry_image = models.ImageField(upload_to='media/ministries')
    ministry_description = models.TextField()
    ministry_chair = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "ministries"

    def __str__(self):
        return f"{self.ministry_name}"

#This is the E-Teams model, for adding the E-Teams in the admin panel
class Eteam(models.Model):
    team_name =  models.CharField(max_length=100)
    team_image = models.ImageField(upload_to='media/ministries')
    team_description = models.TextField()
    team_chair = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.team_name}"

#This is the Images model, It has been used to assist in adding images in the gallery page
class Image(models.Model):
    image = models.ImageField(upload_to= 'media/gallery')
    image_category = models.CharField(max_length=50, choices=IMAGE_CATEGORIES)
    image_to_show_on_website = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.image_category}- {self.id}  {self.image}"
