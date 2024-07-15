"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
admin.site_title = 'GEUZA '
admin.site.site_header = 'GUEZA '
admin.site.index_title = 'Welcome to Gueza '
admin.autodiscover()
urlpatterns = [
    #path('', include('maps.urls')),
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    # path('admin_tools_stats/', include('admin_tools_stats.urls')),
    
    
    #path('adminlte/some_url/', adminlte_views.some_view, name='some_view'),
    # ...
    # Include the app's URLs
    # ... other URL patterns for your project
]

