from django.urls import path
from . import views

urlpatterns = [
   path('education', views.education, name='education'),
   path('school', views.school, name='school'),
   path('university', views.university, name='university'),
   path('library', views.library, name='library'),
   path('science', views.science, name='science')
   ]