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

from jsite.models import BlogPost, Tag


# Create your views here.
def index(request):
	try:
		now = datetime.datetime.now()
		print now.year, now.month, now.day
		# TODO Add pub date > today
		posts = BlogPost.objects.filter(postdate__lte=datetime.date(now.year, now.month, now.day)).order_by('-postdate')
	except BlogPost.DoesNotExist:
		posts = None
	return render_to_response("jsite/index.html", {'posts': posts}, context_instance=RequestContext(request))


def about(request):
	return render_to_response("jsite/about.html", {}, context_instance=RequestContext(request))


def post(request, url):
	post = get_object_or_404(BlogPost, url=url)
	now = datetime.datetime.now()
	
	try:
		newer = BlogPost.objects.filter(postdate__gt=datetime.date(post.postdate.year, post.postdate.month, post.postdate.day)).exclude(postdate__gt=datetime.date(now.year, now.month, now.day)).order_by('postdate')[0] # grab the next oldest
		print newer
	except IndexError, BlogPost.DoesNotExist:
		newer = False
	
	try:
		older = BlogPost.objects.filter(postdate__lt=datetime.date(post.postdate.year, post.postdate.month, post.postdate.day)).order_by('-postdate')[0] # grab the next oldest
	except IndexError, BlogPost.DoesNotExist:
		older = False
	
	return render_to_response("jsite/post.html", { 'post' : post, 'older': older, 'newer': newer }, context_instance=RequestContext(request))


