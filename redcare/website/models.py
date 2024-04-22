from django.contrib.auth.models import AbstractUser
from django.db import models

BLOOD_GROUP_CHOICES = [
    ('A+', 'A+'),
    ('A-', 'A-'),
    ('B+', 'B+'),
    ('B-', 'B-'),
    ('AB+', 'AB+'),
    ('AB-', 'AB-'),
    ('O+', 'O+'),
    ('O-', 'O-'),
]
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
]

class Blood(models.Model):
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default="")
    
    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=101, null=True, default="")
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    address = models.CharField(max_length=102, default="")
    phone = models.CharField(max_length=20, default="98762")
    date_of_birth = models.DateField(null=True)
    image = models.ImageField(upload_to='user_images/', null=True, blank=True)
    username = models.CharField(max_length=150, unique=True)  # Adjust the max_length as needed

    def __str__(self):
        return self.username

class RequestBlood(models.Model):
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.TextField(null='true')
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, default="")
    date = models.DateField()

    def __str__(self):
        return {self.city}
    


    



