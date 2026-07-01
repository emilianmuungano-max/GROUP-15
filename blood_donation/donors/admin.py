from django.contrib import admin
from .models import Donor, Donation, BloodRequest

admin.site.register(Donor)
admin.site.register(Donation)
admin.site.register(BloodRequest)

# Register your models here.
