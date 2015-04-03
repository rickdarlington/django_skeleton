from django.conf.urls import patterns, include, url, include

from beta.views import Signup, Confirmation

urlpatterns = [
    url(
        regex = '^signup/$',
        view = Signup.as_view(),
        name = 'beta_signup',
        ),
    url(
        regex = '^signup/confirmed/$',
        view = Confirmation.as_view(),
        name = 'beta_confirmation',
        ),
    ]
