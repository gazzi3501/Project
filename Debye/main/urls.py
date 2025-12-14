from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='home'),
   path('posetitelam', views.posetitelam, name='posetitelam'), 
   path('contacts', views.contacts, name='contacts'),
   path('education', views.education, name='education'),
   path('programs', views.programs, name='programs'),
   path('store', views.store, name='store'),
   path('always', views.always, name='always'),
   path('temporary', views.temporary, name='temporary'),
   path('online', views.online, name='online'),
]
