from django.conf.urls import url, include
from users.views import dashboard

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
]