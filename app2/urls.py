from django.urls import path
from app2.views import *
app_name='dj'
urlpatterns=[
    path('django/',django,name='django'),
]