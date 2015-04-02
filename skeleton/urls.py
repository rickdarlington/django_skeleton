from django.conf.urls import patterns, include, url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse
from registration.backends.simple.views import RegistrationView

admin.autodiscover()

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),

    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),

	url(r'^$', 'skeleton.views.home', name='home'),
    url(r'^accounts/profile/$', 'skeleton.views.home', name='home'),
]
