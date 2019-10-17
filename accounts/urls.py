from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from django.urls import path, include
from accounts import views
from django.contrib.auth.views import (
LoginView, LogoutView)
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [       
path('login/', views.login, name="login"),

 url(r'^login/$', LoginView, {'template_name':'login.html'}),   
		 url(r'^accounts/profile/view-results/$', views.view_results, name='view_results'),
url(r'^accounts/profile/view-resultss/$', views.view_resultss, name='view_resultss'),
  url(r'^accounts/login/$', LoginView, {'template_name':'login.html'}),      
url(r'^profile/view-results/$', views.view_results, name='view_results'),    
url(r'^profile/view-resultss/$', views.view_resultss, name='view_resultss'),
  
   url(r'^accounts/profile/password/$', views.change_password, name='change_password'),   
  url(r'^profile/password/$', views.change_password, name='change_password'),   
  url(r'^accounts/profile/$', views.view_profile, name='view_profile'),  
    url(r'^profile/$', views.view_profile, name='view_profile'), 
 url(r'^profiles/$', views.index, name='index'), 

 url(r'^profiles/$', views.index, name='index'), 
url(r'^profile/$', views.view_profile, name='view_profile'),    
       url(r'^register/$', views.register, name='register'),

        
            
           url(r'^profile/edit/$', views.edit_profile, name='profile_edit'),
                url(r'^accounts/profile/edit/$', views.edit_profile, name='profile_edit'),
            url(r'^login/register/$', views.register, name='register'),  
        url(r'^success/$', views.success, name='success'),
         
        path('logout/', LogoutView),
           
                       
        	  
              url(r'^accounts/$', views.accounts),
              url(r'^register/register-cont/$', views.register_cont, name='register_cont'),
              
              url(r'^accounts/profile2/$', views.profile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)