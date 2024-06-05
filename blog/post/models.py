from django.db import models

# Create your models here.
class Post(models.Model):
    owner = models.ForeignKey('accounts.CustomUser', verbose_name='投稿者',on_delete=models.CASCADE)
    content = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField('accounts.CustomUser',related_name='related_post',blank=True)

    class Meta:
        db_table = 'posts'

