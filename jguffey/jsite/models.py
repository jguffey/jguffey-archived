from django.db import models

# Create your models here.
class BlogPost(model.Model):
	class Meta:
		verbose_name = 'Blog Post'
		verbose_name_plural = 'Blog Posts'
	title = models.CharField(max_length = 250)
	content = models.TextField()
	postdate = models.DateField(auto_now_add=True, verbose_name="Posted On:", null=True, blank=True)
	modifieddate = models.DateField(auto_now_add=True, verbose_name="Posted On:", null=True, blank=True)
	url = models.CharField(max_length = 250)
	files = models.FileField(upload_to='blog')
	def __unicode__(self):
		return """%s""" % self.title

class Tag(model.Model):
	tag = models.CharField(max_length = 250)
	blogpost = models.ForeignKey(BlogPost)
	def __unicode__(self):
		return """%s""" % self.tag