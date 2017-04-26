from django.conf.urls import url
from .mainviews import views

urlpatterns = [
    url(r'^$', views.current_datetime, name='home'),
]