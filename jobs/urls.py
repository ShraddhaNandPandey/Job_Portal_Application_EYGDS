# jobs/urls.py

from django.urls import path
from .views import landing_page  # Assuming you have a landing page view

urlpatterns = [
    path('', landing_page, name='home'),  # Define the URL pattern with the name 'home'
]
