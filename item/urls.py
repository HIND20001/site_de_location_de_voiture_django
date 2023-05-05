from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('',views.items, name='items'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/reserve_car', views.reserve_car, name='reserve_car'),
    #path('<int:pk>/res_confirm', views.res_confirm , name='res_confirm'),
    path('res', views.user_reservations, name='user_reservations'),
    path('<int:pk>/cancel' , views.user_canc_reservation, name='user_canc_reservation'),
    path('dash', views.admin_dash, name='admin_dash'),
    path('<int:pk>/dele', views.admin_dele_res, name='admin_dele_res'),

]

