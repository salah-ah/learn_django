from django.urls import path
from . import views

# create a URLconf in the demoapp directory
urlpatterns = [
    path('', views.say_hello, name='hello'),
]

