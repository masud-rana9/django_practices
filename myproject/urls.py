
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/',include('first.urls')),
    path('second/',include('second.urls')),
    path('third/',include('third.urls')),
    path('fourth/',include('fourth.urls')),
]
