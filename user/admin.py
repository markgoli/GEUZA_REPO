from django.contrib import admin
from django.utils import timezone
from django.contrib import admin
from .models import UploadedImage, Event, Devotion, DonationCause, SiteVisit, RecentSermon, Ministry
from .forms import DonationCauseForm
from .forms import EventAdmin
#from mapbox_location_field.admin import MapAdmin
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields
from django.contrib import admin
from django.utils.html import format_html
from .models import Devotion
from admin_tools.dashboard import Dashboard
from .dashboard import CustomDashboard
from django.contrib.admin import AdminSite
from .models import TrafficData, SiteVisit, User


class CustomAdminSite(AdminSite):
    site_title = 'Geuza'  # Change this to your desired title
    site_header = 'Geuza '  # Change this to your desired header
    index_title = 'Welcome to Geuza'  # Change this to your desired index title

custom_admin_site = CustomAdminSite(name='customadmin')

class RentalAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'contact', 'address', 'remaining_days')
    formfield_overrides = {
        map_fields.AddressField: {
          'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    }

class DonationCauseAdmin(admin.ModelAdmin):
    form = DonationCauseForm

class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('display_photo','caption', 'uploaded_by', 'uploaded_at')
    readonly_fields = ('uploaded_at', 'uploaded_by')

    def save_model(self, request, obj, form, change):
        if not change:
            # This is a new instance, set the uploaded_by field
            obj.uploaded_by = request.user

        # Always update the updated_by and updated_at fields
        obj.uploaded_by = request.user
        obj.uploaded_at = timezone.now()

        super(UploadedImageAdmin, self).save_model(request, obj, form, change)

    def display_photo(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url) if obj.image else ''

    display_photo.short_description = 'Photo Preview'

class RecentSermonAdmin(admin.ModelAdmin):
    list_display = ('theme', 'date', 'preacher', 'display_photo')

    def display_photo(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.photo.url) if obj.photo else ''

    display_photo.short_description = 'Photo Preview'


class DevotionAdmin(admin.ModelAdmin):
    list_display = ('author', 'scripture', 'date', 'display_photo')

    def display_photo(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.photo.url) if obj.photo else ''

    display_photo.short_description = 'Photo Preview'


class MinistryAdmin(admin.ModelAdmin):
    list_display = ('ministry_name', 'ministry_date', 'ministry_goal', 'display_photo')

    def display_photo(self, obj):
        return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.ministry_photo.url) if obj.ministry_photo else ''

    display_photo.short_description = 'Photo Preview'
from django.contrib import admin
from django.utils.html import mark_safe
import plotly.express as px
from django.db.models import Count
from .models import SiteVisit

class SiteVisitAdmin(admin.ModelAdmin):
    list_display = ('ip_address',)
    change_list_template = "admin/user/sitevisit/change_list.html"  # Ensure this matches your app name and directory

    def changelist_view(self, request, extra_context=None):
        # Aggregate the site visit data per day
        data = SiteVisit.objects.extra(select={'day': "date(timestamp)"}).values('day').annotate(count=Count('counter')).order_by('day')

        # Prepare data for plotting
        dates = [item['day'] for item in data]
        counts = [item['count'] for item in data]

        # Create the plot
        fig = px.line(x=dates, y=counts, labels={'x': 'Date', 'y': 'Number of Visits'})
        graph_html = fig.to_html(full_html=False)

        extra_context = extra_context or {}
        extra_context['graph'] = mark_safe(graph_html)  # Use mark_safe instead of format_html

        return super().changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

# Register the admin class but not the model itself
admin.site.register(SiteVisit, SiteVisitAdmin)

# Unregister the model to hide it from the admin index page
# admin.site.unregister(SiteVisit)



admin.site.register(Devotion, DevotionAdmin)
admin.site.register(RecentSermon, RecentSermonAdmin)
admin.site.register(UploadedImage, UploadedImageAdmin)
admin.site.register(Event, RentalAdmin)
#admin.site.register(Devotion)
admin.site.register(DonationCause, DonationCauseAdmin)
#admin.site.register(RecentSermon)
admin.site.register(Ministry, MinistryAdmin)
# admin.py
# admin.site.register(SiteVisit, SiteVisitAdmin)
#admin.site.register(EventAdmin)
# admin.site.register(CustomDashboard, Dashboard)

# admin.py
from django.contrib import admin
from .models import TrafficData

class TrafficDataAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'path', 'method', 'ip_address', 'user_agent')
    list_filter = ('method', 'timestamp')
    search_fields = ('path', 'ip_address', 'user_agent')
    readonly_fields = ('timestamp', 'path', 'method', 'ip_address', 'user_agent')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

admin.site.register(TrafficData, TrafficDataAdmin)


# admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
import plotly.express as px
from .models import TrafficData, User  # Assuming the User model is already defined
# admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
import plotly.express as px
from .models import TrafficData, User  # Assuming the User model is already defined

class CustomAdmin(admin.ModelAdmin):
    change_list_template = "admin/traffic_data_change_list.html"

    def changelist_view(self, request, extra_context=None):
        # Check if the request is to display the graph
        show_graph = request.GET.get('graph', 'false') == 'true'

        if show_graph:
            # Aggregate the user registration data per day
            data = User.objects.extra(select={'day': "date(registered_at)"}).values('day').annotate(count=models.Count('id')).order_by('day')

            # Prepare data for plotting
            dates = [item['day'] for item in data]
            counts = [item['count'] for item in data]

            # Create the plot
            fig = px.line(x=dates, y=counts, labels={'x': 'Date', 'y': 'Number of Registered Users'})
            graph_html = fig.to_html(full_html=False)

            extra_context = extra_context or {}
            extra_context['graph'] = format_html(graph_html)

        return super().changelist_view(request, extra_context=extra_context)

# admin.site.register(CustomAdmin)
# admin.py
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.utils.html import format_html
import plotly.express as px
from .models import TrafficData, User  # Assuming the User model is already defined

class TrafficDataAdmin(admin.ModelAdmin):
    change_list_template = "admin/your_app/trafficdata/change_list.html"

    def changelist_view(self, request, extra_context=None):
        # Aggregate the user registration data per day
        data = User.objects.extra(select={'day': "date(registered_at)"}).values('day').annotate(count=models.Count('id')).order_by('day')

        # Prepare data for plotting
        dates = [item['day'] for item in data]
        counts = [item['count'] for item in data]

        # Create the plot
        fig = px.line(x=dates, y=counts, labels={'x': 'Date', 'y': 'Number of Registered Users'})
        graph_html = fig.to_html(full_html=False)

        extra_context = extra_context or {}
        extra_context['graph'] = format_html(graph_html)

        return super().changelist_view(request, extra_context=extra_context)

# admin.site.register(TrafficDataAdmin)

# admin.py

from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ('email', 'submitted_at', 'message')
    search_fields = ('email',)
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
