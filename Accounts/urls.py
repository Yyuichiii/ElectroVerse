from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('register/', views.registration,name='registration'),
    path('logout/', views.logout_view,name='logout'),
    path('cart/', views.cart_view,name='Cart'),
    path('remove_cart/<int:id>/', views.remove_cart,name='Remove_Cart'),
    
]

htmxpattern=[
    path('addcart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('qupdt/<str:c>/<int:id>/', views.qupdt, name='quantity_update'),
]

urlpatterns+=htmxpattern