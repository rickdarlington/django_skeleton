from django.conf.urls import patterns, include, url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.core.urlresolvers import reverse

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/', include('allauth.urls')),

    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),

	url(r'^$', 'skeleton.views.home', name='home'),

	#TODO update profile view
    url(r'^accounts/profile/$', 'skeleton.views.home', name='home'),

    #TODO login required example
	url(r'^loginrequired/$', 'skeleton.views.loginrequired', name='home'),    

	#TODO remove django-beta for release
	url(r'^beta/', include('beta.urls')),
]

# ^admin/
# ^accounts/ ^ ^signup/$ [name='account_signup']
# ^accounts/ ^ ^login/$ [name='account_login']
# ^accounts/ ^ ^logout/$ [name='account_logout']
# ^accounts/ ^ ^password/change/$ [name='account_change_password']
# ^accounts/ ^ ^password/set/$ [name='account_set_password']
# ^accounts/ ^ ^inactive/$ [name='account_inactive']
# ^accounts/ ^ ^email/$ [name='account_email']
# ^accounts/ ^ ^confirm-email/$ [name='account_email_verification_sent']
# ^accounts/ ^ ^confirm-email/(?P<key>\w+)/$ [name='account_confirm_email']
# ^accounts/ ^ ^confirm_email/(?P<key>\w+)/$
# ^accounts/ ^ ^password/reset/$ [name='account_reset_password']
# ^accounts/ ^ ^password/reset/done/$ [name='account_reset_password_done']
# ^accounts/ ^ ^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$ [name='account_reset_password_from_key']
# ^accounts/ ^ ^password/reset/key/done/$ [name='account_reset_password_from_key_done']
# ^accounts/ ^social/
# ^logout/$ [name='logout']
# ^login/$ [name='login']
# ^$ [name='home']
# ^accounts/profile/$ [name='home']