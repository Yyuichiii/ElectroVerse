from django.urls import path
from . import views
urlpatterns = [
    path('passive/<str:type>/', views.passive,name='passive'),
    path('active/<str:type>/', views.active,name='active'),
    path('Electromechanical/<str:type>/', views.electromechanical,name='Electromechanical'),
    path('Display/<str:type>/', views.display,name='Display'),
    path('Sensor/<str:type>/', views.sensor,name='Sensor'),
]