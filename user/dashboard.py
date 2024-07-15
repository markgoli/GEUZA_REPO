# user/dashboard.py

from django.utils.translation import gettext_lazy as _
from admin_tools.dashboard import modules, Dashboard, AppIndexDashboard
from django_plotly_dash import DjangoDash
from django.db.models import Count
from user.models import SiteVisit
import plotly.express as px
import pandas as pd  # Import pandas

app = DjangoDash('SiteVisitsApp')  # Unique name for the app

# Fetch data from the SiteVisit model
site_visits_data = SiteVisit.objects.all().order_by('timestamp')

# Convert the queryset to a pandas DataFrame
df = pd.DataFrame.from_records(site_visits_data.values())

fig = px.line(df, x='timestamp', y='counter', title='Site Visits')
fig.update_xaxes(title_text='Timestamp')
fig.update_yaxes(title_text='Counter')
app.layout = fig

class SiteVisitsDashboardModule(modules.DashboardModule):
    title = _('Site Visits Chart')
    template = 'admin_tools/dashboard/modules/chart.html'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# Custom AppIndexDashboard to include the SiteVisitsDashboardModule
class CustomAppIndexDashboard(AppIndexDashboard):
    modules = (SiteVisitsDashboardModule,)

# Custom Dashboard to include the AppIndexDashboard
class CustomDashboard(Dashboard):
    def init_with_context(self, context):
        self.available_children.append(CustomAppIndexDashboard)
