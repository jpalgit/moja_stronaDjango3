from django.urls import path
from . import views

app_name = 'fizyka'  # przestrzeń nazw!! pozwala zorganizować adresy URL według aplikacji
# i używać nazwy aplikacji  podczas  odwoływania  się  do  nich.

urlpatterns = [
   path('termodynamika/', views.termodynamika, name='termodynamika'),
]
