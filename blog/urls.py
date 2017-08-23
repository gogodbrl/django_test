from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^data$', views.data, name='data'),
    url(r'^d3sample$', views.d3sample, name='d3sample'),
    url(r'^d3test$', views.d3test, name='d3test'),
    ]