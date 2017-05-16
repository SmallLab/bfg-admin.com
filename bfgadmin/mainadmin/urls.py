from django.conf.urls import url, include
from .mainviews import views

users_patterns = [
    url(r'^(?:page/(?P<page>\d+)/)?$', views.UsersWork.as_view(), name='users'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='detail'),
    url(r'^ajaxuser/isactive/(?P<pk>[0-9]+)/$', views.AjaxUserIsActiveView.as_view(), name='ajax_is_active'),
]

type_sent_patterns = [
    url(r'^$', views.TypeSentWork.as_view(), name='typesent'),
    url(r'^ajaxts/isactive/(?P<pk>[0-9]+)/$', views.AjaxTypeSentenseActive.as_view(), name='ajax_ts_is_active'),
    url(r'^ajaxts/addnew/$', views.AjaxTypeSentenseNew.as_view(), name='ajax_ts_new'),
    url(r'^deleteset/(?P<pk>[0-9]+)/$', views.TypeSentenceDelete.as_view(), name='delete_ts'),
]


urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='home'),
    url(r'^users/', include(users_patterns)),
    url(r'^typesent/', include(type_sent_patterns)),
]