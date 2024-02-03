from django.urls import path
from . import views
urlpatterns = [
    path('passive/<str:type>/', views.passive,name='passive'),
    # path('register/', views.registration,name='registration'),
    # path('logout/', views.logout_view,name='logout'),

]