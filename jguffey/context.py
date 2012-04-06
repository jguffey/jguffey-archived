from django.template import RequestContext, Context
from django.contrib.sites.models import Site

def getCurrUrl(request):
	try:
		return request.path
	except KeyError:
		return '/'


#example of a global context
#use {{copyright}} in any template now.
def context(request):
	current_site = Site.objects.get_current()
	return {'redirect':getCurrUrl(request), 'colors': ["red", "blue", "purp", "brn", "gol", "grn",], 'url': current_site.domain }