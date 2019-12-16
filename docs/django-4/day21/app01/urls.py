from django.conf.urls import url
from app01 import views



urlpatterns = [
    url(r'^index/',views.index),
]