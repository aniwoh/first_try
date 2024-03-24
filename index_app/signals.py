from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Comments,MarkdownFilePool

@receiver([post_save, post_delete], sender=Comments)
def update_post_comment_count(sender, instance, **kwargs):
    article_id = instance.article_id
    article = MarkdownFilePool.objects.get(id=article_id)
    article.comment_count = Comments.objects.filter(article_id=article_id).count()
    article.save()