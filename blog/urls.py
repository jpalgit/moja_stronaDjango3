from django.urls import path
from . import views

app_name = 'blog'  # przestrzeń nazw!! pozwala zorganizować adresy URL według aplikacji
# i używać nazwy aplikacji  podczas  odwoływania  się  do  nich.

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.lista_postow, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]

