from django.conf.urls import url,include
from django.contrib import admin

from app import views as app_views

urlpatterns = [

    url(r'^', include('app.urls')),
    url(r'^admin/', admin.site.urls),
]