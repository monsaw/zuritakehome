from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 400)
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    body = models.TextField()


    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs = {"pk":self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('POST', on_delete = models.CASCADE , related_name = 'comments')
    author = models.CharField(max_length = 50)
    body = models.TextField()
    date = models.DateTimeField(default = timezone.now())

    def get_absolute_url(self):
        return reverse('blog:post_detail',kwargs = {"pk":self.pk})

    def __str__(self):
        return self.author
