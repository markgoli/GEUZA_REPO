from django.utils import timezone
from .models import SiteVisit

class SiteVisitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Track site visit
        site_visit, created = SiteVisit.objects.get_or_create(date=timezone.now().date())
        site_visit.counter += 1
        site_visit.save()

        response = self.get_response(request)
        return response
