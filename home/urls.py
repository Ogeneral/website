from django.conf.urls import url
from home import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [      
       url(r'^$', views.home),
       url(r'^gallery', views.gallery),
       url(r'^wywlu', views.wywlu, name='wywlu'),
        url(r'^know_more', views.more, name='more'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
