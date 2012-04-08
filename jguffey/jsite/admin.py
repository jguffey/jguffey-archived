from django.db import models
from django.contrib import admin
from jsite.models import BlogPost, Tag
# from tinymce.widgets import TinyMCE



class BlogPostAdmin(admin.ModelAdmin):
	model = BlogPost
	readonly_fields = ("createddate", "modifieddate")
	formfield_overrides = {
		# models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
		# content.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
	}


admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Tag)