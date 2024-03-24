from django.db import models

# Create your models here.
class MarkdownFilePool(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)

class Comments(models.Model):
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    article_id = models.IntegerField()
    author = models.TextField(max_length=20)