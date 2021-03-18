from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class Meta:
        db_table = "users"


class Students(models.Model):
    img = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    Enrollment_number = models.IntegerField()
    gender = models.CharField(max_length=30)
    hobbies = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)

    class Meta:
        db_table = "Students"

