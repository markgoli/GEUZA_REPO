from django.urls import path, include
from .views import about, sermons, index, event, contact_view, map_page, ministries, single_ministries, donation, subscribe, contact_success_view, join
from django.urls import reverse
from django.conf.urls.static import static
from django.conf import settings
# ... your existing urlpatterns ..

# urls.py

# app_name = 'GUEZZA '

urlpatterns = [
    path('', index, name='index'),
    path('geuza/', about, name='geuza'),
    path('sermons/', sermons, name='sermons'),
    path('gevent/', event, name='gevent'),
    path('donate/', donation, name='donate'),
    path('contacts/', contact_view, name='contacts'),
    path('ministries/', ministries, name='ministries'),
    path('ministries_single/', single_ministries, name='mini_single'),
    path('map/', map_page, name='map'),
    path('subscribe/', subscribe, name='subscribe'),
    path('join/', join, name='join'),
    # path('donatex/', donation_page, name='donation_page'),
    # path("djangoflutterwave/", include("djangoflutterwave.urls", namespace="djangoflutterwave")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
