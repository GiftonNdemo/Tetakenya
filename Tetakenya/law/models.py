from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from PIL import Image
# Create your models here.


class User(AbstractUser):
    is_client = models.BooleanField(default=False)
    is_lawyer = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100, null=True)


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    phone_number_validator = RegexValidator(regex=r'^(0|\+)\d{8,15}$')
    Phone_Number = models.CharField(validators=[phone_number_validator], max_length=17, unique=True, null=True)

    def __str__(self):
        return self.first_name


class Lawyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, null=True)
    county = models.CharField(max_length=20, null=True)
    experience = models.IntegerField(default=2)
    profile_pic = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)

    def __str__(self):
        return self.first_name

    def save(self):
        super().save()

        img = Image.open(self.profile_pic.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)


class Service(models.Model):
    lawyer = models.ForeignKey(Lawyer, null=True, on_delete=models.SET_NULL)
    Service_Name = models.CharField(max_length=50)
    Service_Cost = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.Service_Name


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)


