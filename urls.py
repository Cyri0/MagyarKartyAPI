from django.urls import path
from .views import *

urlpatterns = [
    path('', base),
    path('cards/', getcards),
    path('getcard/<str:id>/', getcard),
    path('getdeck/<str:id>/', getdeck),
    path('getnewdeck/', getnewdeck)
]