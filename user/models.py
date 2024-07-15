# models.py
import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
#from mapbox_location_field.models import LocationField
from django.db import models
from django.utils import timezone
#from mapbox_location_field.models import LocationField
from django.core.validators import RegexValidator
from django.contrib.auth.models import Group, User
from django_google_maps import fields as map_fields
from django.db import models

#from location_field.models.plain import PlainLocationField


class CustomGroup(Group):
    class Meta:
        verbose_name_plural = 'Manage Users'

class CustomUser(User):
    class Meta:
        verbose_name_plural = 'Modules'



def get_image_upload_path(instance, filename):
    return os.path.join('images', filename)
class UploadedImage(models.Model):
    image = models.ImageField(upload_to=get_image_upload_path)
    caption = models.CharField(max_length=255)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='uploaded_images', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='updated_images')
    # updated_at = models.DateTimeField(null=True, auto_now_add=True)

    def __str__(self):
        return self.caption

    def save(self, *args, **kwargs):
        # Set uploaded_by and uploaded_by_name only if it's a new instance and uploaded_by is not already set
        if not self.uploaded_by_id:
            self.uploaded_by = kwargs.pop('user', None)
            
        # Always update the updated_by and updated_at fields
        self.uploaded_by = kwargs.pop('user', None)
        self.uploaded_at = timezone.now()

        super(UploadedImage, self).save(*args, **kwargs)

    @classmethod
    def import_and_fill_foreign_keys(cls, user):
        # Your logic for importing and filling foreign keys goes here
        pass

    class Meta:
        verbose_name = 'Home Page Photo'
        verbose_name_plural = 'Home Page Photos'

from django.db import models
from django.utils import timezone
from django.db import models
from django.utils import timezone
from django.utils import timezone
# models.py
from django.db import models
from django.utils import timezone

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    description = models.CharField(max_length=100)
    contact = models.CharField(max_length=25)
    address = models.CharField(max_length=200, null=True)
    remaining_days = models.IntegerField(blank=True, null=True)
    link = models.URLField("Google Form Link")  # Auto-calculated field

    def save(self, *args, **kwargs):
        # Calculate remaining days including the time before saving
        event_datetime = timezone.make_aware(timezone.datetime.combine(self.date, self.time))
        remaining_time = event_datetime - timezone.now()
        self.remaining_days = max(remaining_time.days, 0)  # Ensure remaining_days is non-negative
        super().save(*args, **kwargs)

    @property
    def datetime(self):
        return timezone.make_aware(timezone.datetime.combine(self.date, self.time))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Event Detail'
        verbose_name_plural = 'Event Details'




        
class Devotion(models.Model):
    photo = models.ImageField(upload_to=get_image_upload_path)
    Theme = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    scripture = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} - {self.scripture}'
    
    class Meta:
        verbose_name = 'Devotion'
        verbose_name_plural = 'Devotions'
        
class DonationCause(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateField()

    # Validator for contacts field: Allows only numbers with an optional country code (e.g., +123456789)
    contacts_validator = RegexValidator(
        regex=r'^\+(\d{1,15})$',
        message='Enter a valid phone number with country code. Example: +123456789',
    )

    contacts = models.CharField(max_length=16, validators=[contacts_validator])
    details = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Donation Cause'
        verbose_name_plural = 'Donation Cuase'
        
# models.py
from django.db import models

class SiteVisit(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField(auto_now_add=True)
    counter = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.ip_address} - {self.timestamp}"

# from PIL import Image
# from django.utils.html import format_html

# def display_image_thumbnail(self):
#     try:
#         img = Image.open(self.sermon_picture.path)
#         img.thumbnail((50, 50)) # Adjust the size as needed
#         return format_html('<img src="{}" width="{}" height="{}" />', img.url, img.width, img.height)
#         except IOError:
#             return "Image not available"

# display_image_thumbnail.short_description = 'Thumbnail'

class Ministry(models.Model):
    ministry_name = models.CharField(max_length=25)
    ministry_photo = models.ImageField(upload_to='ministry_photos/', blank=True, null=True)
    ministry_goal = models.TextField(blank=False)
    ministry_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ministry_name


class RecentSermon(models.Model):
    theme = models.CharField(max_length=40)
    date = models.DateField()
    short_description = models.TextField(blank=False, max_length= 100)
    preacher = models.CharField(max_length=25)
    preachers_title =models.CharField(max_length=10)
    photo = models.ImageField(upload_to='recent_sermon_photos/')

    def __str__(self):
        return f'{self.theme} - {self.date}'

    class Meta:
        verbose_name = 'Gospel'
        verbose_name_plural = 'Gospel Word'


# models.py
from django.db import models

class TrafficData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=10)
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField()

    def __str__(self):
        return f"{self.ip_address} accessed {self.path} on {self.timestamp}"

# models.py

from django.db import models

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

# models.py

from django.db import models

class ContactSubmission(models.Model):
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
