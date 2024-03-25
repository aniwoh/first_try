from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

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

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 添加你的字段
    level = models.IntegerField(default=0)

@receiver(post_save,sender=User) # 监听到post_save事件且发送者是User则执行create_extension_user函数
def create_extension_user(sender,instance,created,**kwargs):
    """
    sender:发送者
    instance:save对象
    created:是否是创建数据
    """
    if created: 
        # 如果创建对象，ExtensionUser进行绑定
        UserProfile.objects.create(user=instance)
    # else:
    #     # 如果不是创建对象，同样将改变进行保存
    #     instance.user.save()