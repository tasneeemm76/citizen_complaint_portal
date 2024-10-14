
from django.db import models
class register(models.Model):
    username = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    code_word=models.CharField(max_length=200)
    aadhar=models.CharField(max_length=12)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    pin=models.IntegerField()

    class Meta:
        db_table='citizen'

from django.db import models
from geopy.geocoders import Nominatim

class ReportedIssue(models.Model):
    ISSUE_TYPES = [
        ('Sanitation', 'Sanitation'),
        ('Infrastructure', 'Infrastructure'),
        ('Public Safety', 'Public Safety'),
        ('Traffic', 'Traffic'),
        ('Other', 'Other'),
    ]

    SUBTYPES_SANITATION = [
        ('Garbage not collected', 'Garbage not collected'),
        ('Water clogging', 'Water clogging'),
        ('Improper drainage', 'Improper drainage'),
    ]

    SUBTYPES_INFRASTRUCTURE = [
        ('Potholes', 'Potholes'),
        ('Streetlight broken', 'Streetlight broken'),
        ('Damaged road', 'Damaged road'),
    ]
    issue_id=models.AutoField(primary_key=True)
    issue_type = models.CharField(max_length=100, choices=ISSUE_TYPES, default='Other')
    issue_subtype = models.CharField(max_length=100)
    issue_description = models.TextField(blank=True)
    area_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    latitude = models.FloatField(null=True, blank=True)  # Added for geocoding
    longitude = models.FloatField(null=True, blank=True)  # Added for geocoding
    submission_date = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f'{self.issue_type} - {self.issue_subtype} in {self.area_name} ({self.pincode})'

    def save(self, *args, **kwargs):
        # Geocode the pincode if latitude and longitude are not provided
        if not self.latitude or not self.longitude:
            geolocator = Nominatim(user_agent="smartcity_geocoder")
            location = geolocator.geocode(self.pincode)
            if location:
                self.latitude = location.latitude
                self.longitude = location.longitude
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'reported_issues'