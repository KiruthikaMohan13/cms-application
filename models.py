from django.db import models
from django.urls import reverse
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(null=True,blank=True)
	content = models.TextField()
	update = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("posts:post_detail",kwargs={"id":self.id})