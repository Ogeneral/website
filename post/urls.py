from django.conf.urls import url
from post import views


urlpatterns = [     
url(r'^posts/$', views.index),
url(r'^posts/(?P<post_id>\d+)/$', views.detail),
url(r'^posts/(?P<post_id>\d+)/comment/$', views.add_comment),
url(r'^comment/$', views.add_comment),
url(r'^add-post/$', views.add_post),
]