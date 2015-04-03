from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import View
from django.contrib import messages

from beta.models import BetaSignup 
from beta.forms import BetaSignupForm

class Signup(generic.CreateView):
    """ View to handle beta signup """
    template_name = 'beta/signup.html' 
    form_class = BetaSignupForm

    def get_success_url(self):
    	messages.add_message(self.request, messages.INFO, 'Thanks for your interest!')
        return "/"

class Confirmation(generic.TemplateView):
    """ Confirmation Page """
    template_name = 'beta/confirmation.html'

