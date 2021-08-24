from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('create/',views.create_colleted_data, name='create'),
    path('create/',views.create_colleted_data, name='update'),


]
