#This Route/Url configuration Controll and reffered to all the other app urls 

from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from donation import views 


urlpatterns = [
     #url(r'^admin/', admin.site.urls),
    url(r'^admin/', include('dashboard.urls')),
    url(r'^api/', include('api.urls')),


    #Authentication URLS #Don touch other url for your api rout #Checked #Date-10-11-2017
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^social-auth/', include('rest_framework_social_oauth2.urls')),
    url(r'^api/v1/rest-auth/', include('rest_auth.urls')),
    url(r'^api/v1/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/v1/rest-auth/facebook/$', views.FacebookLogin.as_view(), name='fb_login'),
    url(r'^api/v1/rest-auth/twitter/$', views.TwitterLogin.as_view(), name='twitter_login'),
    url(r'^api/v1/rest-auth/google/$', views.GoogleLogin.as_view(), name='google_login'),
    url(r'^accounts/', include('allauth.urls'), name='socialaccount_signup'),
    # url(r'^', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
