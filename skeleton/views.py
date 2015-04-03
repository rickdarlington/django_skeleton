from django.http import HttpResponse, Http404
from django.shortcuts import render, render_to_response, RequestContext
from django.contrib.auth.decorators import login_required

from emailauth.models import MyUser

import logging
logger = logging.getLogger(__name__)

#standard views here
def home(request):
	return render_to_response("home.html", locals(), context_instance=RequestContext(request))

def login(request):
	return render_to_response("login.html", locals(), context_instance=RequestContext(request))    

@login_required
def loginrequired(request):
	some_text = "hi there!"
	return render_to_response("loginrequired.html", locals(), context_instance=RequestContext(request))

def about(request):
	return render_to_response("about.html", locals(), context_instance=RequestContext(request))

#TODO remove intro for launch
def intro(request):
	return render_to_response("intro.html", locals(), context_instance=RequestContext(request))