from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    objects = models.Manager() 

    USER_ROLES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
        ('patient', 'Patient'),
        ('admin', 'Admin'),
    ]

    UserID = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=255)
    UserRole = models.CharField(max_length=10, choices=USER_ROLES)
    RegistrationDate = models.DateTimeField()
    Address = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=15)

    # password hasher
    def save(self, *args, **kwargs):
        self.Password = make_password(self.Password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
