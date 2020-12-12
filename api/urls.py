from .views import RoomView
from django.urls import path

urlpatterns = [
    path('home', RoomView.as_view()),
]
