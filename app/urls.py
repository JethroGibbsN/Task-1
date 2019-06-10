from django.conf.urls import url
from .views import  signupform
from app import views as app_views

urlpatterns = [

    url(r'^', signupform),

]