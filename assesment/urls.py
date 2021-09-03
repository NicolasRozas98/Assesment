from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('',views.create_colleted_data, name='send'),
]
