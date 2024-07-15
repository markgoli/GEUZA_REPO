# # analytics/middleware.py

# from .models import Visitor

# class VisitorMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Get user IP address
#         ip_address = request.META.get('REMOTE_ADDR', None)

#         # Create a new Visitor instance
#         visitor = Visitor(ip_address=ip_address)
#         if request.user.is_authenticated:
#             visitor.user = request.user

#         # Save the Visitor instance
#         visitor.save()

#         response = self.get_response(request)
#         return response

# analytics/middleware.py

# analytics/middleware.py

from .models import SiteVisit

class VisitorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get user IP address
        ip_address = request.META.get('REMOTE_ADDR', None)

        # Create or update a SiteVisit instance
        site_visit, created = SiteVisit.objects.get_or_create(ip_address=ip_address)
        site_visit.counter += 1
        site_visit.save()

        response = self.get_response(request)
        return response

# middleware.py
from .models import TrafficData

class TrafficLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.method in ['GET', 'POST']:  # You can log other methods as well if needed
            TrafficData.objects.create(
                path=request.path,
                method=request.method,
                ip_address=request.META.get('REMOTE_ADDR'),
                user_agent=request.META.get('HTTP_USER_AGENT', ''),
            )
        
        return response
