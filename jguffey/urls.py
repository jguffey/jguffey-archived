from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.contrib.auth.views import password_reset
from jsite import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'jguffey.views.home', name='home'),
    # url(r'^jguffey/', include('jguffey.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('jsite.views',
	url(r'^$', 'index'),
	url(r'^about/$', 'about'),
	url(r'^post/$', 'post'),
	url(r'^tinymce/', include('tinymce.urls')),
	url(r'^post/(.+)/$', 'post'),
)

if settings.DEBUG is False:   #if DEBUG is True it will be served automatically
	urlpatterns += patterns('',
		url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
	)