from django.urls import path
from app1.views import *
app_name='py'
urlpatterns=[
    path('python/',python,name='python')

]