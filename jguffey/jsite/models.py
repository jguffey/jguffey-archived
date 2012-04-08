from django.db import models

# Create your models here.
class BlogPost(models.Model):
	class Meta:
		verbose_name = 'Blog Post'
		verbose_name_plural = 'Blog Posts'
	title = models.CharField(max_length = 250)
	exerpt = models.TextField()
	content = models.TextField()
	postdate = models.DateField(verbose_name="Post On", blank=True)
	modifieddate = models.DateField(auto_now=True, verbose_name="Edited On", blank=True)
	createddate = models.DateField(auto_now_add=True, verbose_name="Created On", blank=True)
	url = models.CharField(max_length = 250, null=True, blank=True)
	files = models.FileField(upload_to='blog', null=True, blank=True)
	def __unicode__(self):
		return """%s""" % self.title

class Tag(models.Model):
	tag = models.CharField(max_length = 250)
	blogpost = models.ForeignKey(BlogPost)
	def __unicode__(self):
		return """%s""" % self.tag
