from django.template import RequestContext, Context
from django.contrib.sites.models import Site

import datetime

def getCurrUrl(request):
	try:
		return request.path
	except KeyError:
		return '/'


#example of a global context
#use {{copyright}} in any template now.
def context(request):
	current_site = Site.objects.get_current()
	now = datetime.datetime.now()
	return {'redirect':getCurrUrl(request), 'url': current_site.domain, 'year': "%d" % now.year }