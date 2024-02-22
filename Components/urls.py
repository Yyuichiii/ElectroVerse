from django.urls import path
from . import views
urlpatterns = [
    path('<str:Category>/<str:type>/',views.Components_view,name='Components'),
    path('Products/',views.Products_list_view,name='Products_list'),
    path('Products/<int:pk>',views.Products_Content_view,name='Products_Content'),
]