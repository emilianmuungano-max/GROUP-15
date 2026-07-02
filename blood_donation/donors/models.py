
from django.db import models

class Donor(models.Model):
    BLOOD_GROUPS = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]

    full_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.full_name


class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    donation_date = models.DateField()
    blood_amount_ml = models.IntegerField()
    hospital_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.donor.full_name} - {self.donation_date}"


class BloodRequest(models.Model):
    BLOOD_GROUPS = Donor.BLOOD_GROUPS

    patient_name = models.CharField(max_length=100)
    blood_group_needed = models.CharField(max_length=3, choices=BLOOD_GROUPS)
    units_needed = models.IntegerField()
    hospital_name = models.CharField(max_length=100)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.patient_name
# Create your models here.
