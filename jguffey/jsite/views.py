import mimetypes, os, datetime, smtplib

from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.sites.models import Site
from django.core.mail import send_mail, EmailMultiAlternatives
from django.utils import simplejson
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt






# Create your views here.
def index(request):
	return render_to_response("jsite/index.html", {}, context_instance=RequestContext(request))
	
def about(request):
	return render_to_response("jsite/about.html", {}, context_instance=RequestContext(request))

def post(request):
	return render_to_response("jsite/post.html", {}, context_instance=RequestContext(request))

