from django.conf.urls import patterns, include, url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('allauth.urls')),

	url(r'^$', 'skeleton.views.about', name='home'),

	#TODO update profile view
    url(r'^accounts/profile/$', 'skeleton.views.home', name='home'),

    #TODO login required example
	url(r'^loginrequired/$', 'skeleton.views.loginrequired', name='home'),    

    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^about/$', 'skeleton.views.about', name='home'),	
]