from django.conf.urls import url, include
from .mainviews import views

users_patterns = [
    url(r'^(?:page/(?P<page>\d+)/)?$', views.UsersWork.as_view(), name='users'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='detail'),
    url(r'^ajaxuser/isactive/(?P<pk>[0-9]+)/$', views.AjaxUserIsActiveView.as_view(), name='ajax_is_active'),
]




urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='home'),
    url(r'^users/', include(users_patterns)),
]