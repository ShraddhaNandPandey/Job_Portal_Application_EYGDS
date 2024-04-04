from django.urls import path
from .views import landing_page, register, login, hr_page, hr_post_job, logout_user

urlpatterns = [
    path('', landing_page, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
    path('hr/', hr_page, name='hr_page'),
    path('hr/post-job/', hr_post_job, name='hr_post_job'),
]
