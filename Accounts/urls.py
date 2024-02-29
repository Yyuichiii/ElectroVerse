from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login_view,name='login'),
    path('register/', views.registration,name='registration'),
    path('logout/', views.logout_view,name='logout'),
    path('password_Change/', views.password_change_view,name='Password_Change'),
    path('Profile/', views.Profile_view,name='Profile'),
    path('Address/', views.address_list,name='Address'),
    path('cart/', views.cart_view,name='Cart'),
    path('remove_cart/<int:id>/', views.remove_cart,name='Remove_Cart'),
    
]

htmxpattern=[
    path('addcart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('qupdt/<str:c>/<int:id>/', views.qupdt, name='quantity_update'),
    path('Address_edit/', views.Address_Edit_view.as_view(),name='Address_Edit'),
]

urlpatterns+=htmxpattern