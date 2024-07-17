from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import UploadedImage, Ministry, RecentSermon, Event
from django.utils import timezone

from django.shortcuts import render
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
# views.py
from django.shortcuts import render
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
import validators  # You need to install validators package: pip install validators
# views.py
from django.shortcuts import render
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
import validators
# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscriber
from .forms import SubscriberForm
# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscriber
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
import validators

# views.py
# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscriber
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
import validators
# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Subscriber
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
import validators

def subscribe(request):
    print("Form submitted")  # Debugging line
    if request.method == 'POST':
        email = request.POST.get('email')
        print(f"Email: {email}")  # Debugging line
        if email:
            if not Subscriber.objects.filter(email=email).exists():
                Subscriber.objects.create(email=email)
                send_mail(
                    'Subscription Confirmation',
                    'Thank you for subscribing to our newsletter!',
                    'your_email@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for subscribing to our newsletter!')
            else:
                messages.info(request, 'This email is already subscribed.')
        else:
            messages.error(request, 'Please enter a valid email address.')
    return redirect('home')

def index(request):
    last_image = UploadedImage.objects.last()
    second_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[1]
    third_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[2]
    last_two_sermons = RecentSermon.objects.order_by('-id')[:3]
    all_ministries = Ministry.objects.all()
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now.date()).order_by('date', 'time')
    upcoming_event = upcoming_events.first() if upcoming_events.exists() else None

    for event in upcoming_events:
        event_datetime = timezone.make_aware(timezone.datetime.combine(event.date, event.time))
        event.remaining_days = (event_datetime - now).days if event_datetime > now else 0
        event.is_valid_link = validators.url(event.link) if event.link else False

    context = {
        'last_image': last_image,
        'second_last_image': second_last_image,
        'third_last_image': third_last_image,
        'all_ministries': all_ministries,
        'last_two_sermons': last_two_sermons,
        'upcoming_event': upcoming_event,
        'upcoming_events': upcoming_events,
    }

    # return render(request, 'user/index-corporate.html', context)
    return render(request, 'user/Home.html', context)



# views.py
from django.shortcuts import render
from .models import RecentSermon

def sermons(request):
    all_sermons = RecentSermon.objects.all().order_by('-date')
    context = {
        'all_sermons': all_sermons,
    }
    return render(request, 'user/Sermon.html', context)


def about(request):
    return render(request, 'user/About.html')

# views.py
from django.shortcuts import render
from django.utils import timezone
from .models import UploadedImage, RecentSermon, Ministry, Event
import validators

def event(request):
    last_image = UploadedImage.objects.last()
    second_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[1]
    third_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[2]
    last_two_sermons = RecentSermon.objects.order_by('-id')[:4]
    all_ministries = Ministry.objects.all()
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now.date()).order_by('date', 'time')
    upcoming_event = upcoming_events.first() if upcoming_events.exists() else None

    for event in upcoming_events:
        event_datetime = timezone.make_aware(timezone.datetime.combine(event.date, event.time))
        event.remaining_days = (event_datetime - now).days if event_datetime > now else 0
        event.is_valid_link = validators.url(event.link) if event.link else False

    context = {
        'last_image': last_image,
        'second_last_image': second_last_image,
        'third_last_image': third_last_image,
        'all_ministries': all_ministries,
        'last_two_sermons': last_two_sermons,
        'upcoming_event': upcoming_event,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'user/Events.html', context)

def donation(request):
    last_image = UploadedImage.objects.last()
    second_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[1]
    third_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[2]
    last_two_sermons = RecentSermon.objects.order_by('-id')[:4]
    all_ministries = Ministry.objects.all()
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now.date()).order_by('date', 'time')
    upcoming_event = upcoming_events.first() if upcoming_events.exists() else None

    for event in upcoming_events:
        event_datetime = timezone.make_aware(timezone.datetime.combine(event.date, event.time))
        event.remaining_days = (event_datetime - now).days if event_datetime > now else 0
        event.is_valid_link = validators.url(event.link) if event.link else False

    context = {
        'last_image': last_image,
        'second_last_image': second_last_image,
        'third_last_image': third_last_image,
        'all_ministries': all_ministries,
        'last_two_sermonuser/templates/users': last_two_sermons,
        'upcoming_event': upcoming_event,
        'upcoming_events': upcoming_events,
    }
    return render(request, 'user/Donation.html', context)

def contacts(request):
    return render(request, 'user/Contact.html')

def ministries(request):
    last_image = UploadedImage.objects.last()
    second_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[1]
    third_last_image = UploadedImage.objects.all().order_by('-uploaded_at')[2]
    last_two_sermons = RecentSermon.objects.order_by('-id')[:4]
    all_ministries = Ministry.objects.all()
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now.date()).order_by('date', 'time')
    upcoming_event = upcoming_events.first() if upcoming_events.exists() else None

    for event in upcoming_events:
        event_datetime = timezone.make_aware(timezone.datetime.combine(event.date, event.time))
        event.remaining_days = (event_datetime - now).days if event_datetime > now else 0
        event.is_valid_link = validators.url(event.link) if event.link else False

    context = {
        'last_image': last_image,
        'second_last_image': second_last_image,
        'third_last_image': third_last_image,
        'all_ministries': all_ministries,
        'last_two_sermons': last_two_sermons,
        'upcoming_event': upcoming_event,
        'upcoming_events': upcoming_events,
    }

    return render(request, 'user/Ministry.html', context)

def single_ministries(request):
    return render(request, 'user/MINISTRY_SING.html')


def join(request):
    return render(request, 'user/JoinUs.html')

# from djangoflutterwave.models import FlwPlanModel
# from django.views.generic import TemplateView

# class SignUpView(TemplateView):
#     """Sign Up view"""

#     template_name = "my_payment_template.html"

#     def get_context_data(self, **kwargs):
#         """Add payment type to context data"""
#         kwargs = super().get_context_data(**kwargs)
#         kwargs["pro_plan"] = FlwPlanModel.objects.filter(
#             name="Pro Plan"
#         ).first()
#         return kwargs


# # views.py
# from django.shortcuts import render
# from django.views import View

# class PaymentView(View):
#     template_name = 'HOME.html'

#     def get(self, request, *args, **kwargs):
#         # Retrieve the payment link from Flutterwave or generate it
#         payment_link = "https://sandbox-flw-web-v3.herokuapp.com/donate/uireewoscuvt"

#         # Pass the payment link to the template
#         return render(request, self.template_name, {'payment_link': payment_link})

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Event
#from .forms import SearchForm
import folium # type: ignore
from folium import plugins # type: ignore
import geocoder # type: ignore
import geopy.distance # type: ignore

def calculate_distance(coord1, coord2):
    return geopy.distance.distance(coord1, coord2).km

def map_page(request):
    # if request.method == 'POST':
    #     form = SearchForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('/')
    # else:
    #     form = SearchForm()

    # Retrieve the latest address from the database
    address = Event.objects.all().last()

    # Use geocoder to get the coordinates of the provided address
    location = geocoder.osm(address)
    lat = location.latlng[0] if location.latlng else None
    lng = location.latlng[1] if location.latlng else None
    country = location.country

    # Check if the coordinates are valid
    if lat is None or lng is None:
        address.delete()
        return HttpResponse('Your address input is invalid')

    # Create Map Object centered on the user's input location
    m = folium.Map(location=[lat, lng], zoom_start=12)

    # Add a marker for the user's input location
    user_marker = folium.Marker([lat, lng], tooltip='Your Location', popup=country).add_to(m)
    plugins.MeasureControl(primary_length_unit='kilometers').add_to(m)
    default_location = [0.3363, 32.5682]
    default_marker = folium.Marker(default_location, tooltip='Your location', popup='Makerere University default').add_to(m)
    folium.PolyLine(locations=[[lat, lng], default_location], color='blue').add_to(m)
    distance = calculate_distance((lat, lng), (default_location[0], default_location[1]))

    # Get HTML Representation of Map Object
    m = m._repr_html_()
    context = {
        'm': m,
        # 'form': form,
        'distance': distance,
    }
    return render(request, 'user/map.html', context)
# from django.shortcuts import render
# from django.http import JsonResponse
# from django.db.models import Count
# from .models import SiteVisit
# from datetime import datetime, timedelta

# def site_visits_data(request):
#     # Logic to retrieve daily site visits data

#     # Get the date of one week ago from today
#     one_week_ago = datetime.now() - timedelta(days=7)

#     # Query the database to get daily visit counts for the last week
#     visit_data = SiteVisit.objects.filter(timestamp__gte=one_week_ago)\
#                                   .annotate(date=models.functions.TruncDay('timestamp'))\
#                                   .values('date')\
#                                   .annotate(count=Count('id'))\
#                                   .order_by('date')

#     # Prepare data for JsonResponse
#     labels = [entry['date'].strftime('%Y-%m-%d') for entry in visit_data]
#     values = [entry['count'] for entry in visit_data]

#     data = {'labels': labels, 'values': values}
#     return JsonResponse(data)

# def donations_data(request):
#     # Logic to retrieve monthly donation data
#     # This could be based on your custom model or some other source
#     data = {'labels': ['Jan', 'Feb', 'Mar', ...], 'values': [500, 700, 300, ...]}
#     return JsonResponse(data)

from django.shortcuts import render, redirect
from .forms import ContactForm
from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import ContactSubmission

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Get form data
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # Save to database
            ContactSubmission.objects.create(email=email, message=message)
            # Redirect after POST
            return redirect('contact_success')
    else:
        form = ContactForm()
    return render(request, 'user/Contact.html', {'form': form})



def contact_success_view(request):
    return render(request, 'user/contact_success.html')

