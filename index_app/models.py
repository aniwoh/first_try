from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=100)

# Create your models here.
class MarkdownFilePool(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    thumbs_up = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

class Comments(models.Model):
    content = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    article_id = models.IntegerField()
    author = models.TextField(max_length=20)
    belong_to_comment = models.IntegerField(default=0) # 0 means this comment is a root comment, otherwise it is a reply to a comment
    repeat_someone = models.TextField(max_length=20, default='') # if this comment is a reply to a comment, this field will store the author of the comment
    thumbs_up = models.IntegerField(default=0)
