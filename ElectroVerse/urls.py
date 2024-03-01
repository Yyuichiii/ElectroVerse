from django.contrib import admin
from django.urls import path,include
from Accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('account/',include('Accounts.urls')),
    path('components/',include('Components.urls')),
    path('summernote/', include('django_summernote.urls')),
]
from django.conf.urls.static import static
from django.conf import settings

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)