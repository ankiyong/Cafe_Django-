from django.urls import path
from . import views


urlpatterns = [
    path('send/',views.sendEmail), #http://127.0.0.1:8000/sendEmail/send/
]