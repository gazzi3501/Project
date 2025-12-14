from django.urls import path
from . import views

urlpatterns = [
   path('programms', views.programms, name='programms'),
   path('afisha', views.afisha, name='afisha'),
   path('lectures', views.lectures, name='lectures'),
   path('masterclass', views.masterclass, name='masterclass')
]