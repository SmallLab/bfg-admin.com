from django.conf.urls import url, include
from .mainviews import views

users_patterns = [
    url(r'^(?:page/(?P<page>\d+)/)?$', views.UsersWork.as_view(), name='users'),
    url(r'^detail/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='detail'),
    url(r'^ajaxuser/isactive/(?P<pk>[0-9]+)/$', views.AjaxUserIsActiveView.as_view(), name='ajax_is_active'),
]

"""
    URL`s for CTR(Category, Regions, Type Sentences)
"""
ctr_patterns = [
    url(r'^ajaxctr/isactive/(?P<pk>[0-9]+)/$', views.AjaxCtrActive.as_view(), name='ajax_ctr_is_active'),
    url(r'^ajaxctr/addnew/$', views.AjaxCtrNew.as_view(), name='ajax_ctr_new'),
    url(r'^deletectr/(?P<pk>[0-9]+)/$', views.CtrDelete.as_view(), name='delete_ctr'),
    url(r'^(?P<type_slug>[\w]*)?/', views.CtrWork.as_view(), name='ctr'),
]



urlpatterns = [
    url(r'^$', views.MainView.as_view(), name='home'),
    url(r'^users/', include(users_patterns)),
    url(r'^ctr/', include(ctr_patterns)),

    url(r'^typesent/', include(type_sent_patterns)),
    url(r'^category/', include(category_patterns)),
    url(r'^region/', include(region_patterns)),
]