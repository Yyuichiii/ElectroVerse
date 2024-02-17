from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('register/', views.registration,name='registration'),
    path('logout/', views.logout_view,name='logout'),
    path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
]

