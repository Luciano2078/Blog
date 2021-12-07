from django.db import models

from .models import Post


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=80)
    email  = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)


    class Meta:
        ordering =['created']


    def __str__(self):
        return 'comment {} by {}'.format(self.body, self.name)

