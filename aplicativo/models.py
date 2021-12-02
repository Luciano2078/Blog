from django.db import models

from django.contrib.auth.models import User

from django.urls import reverse

STATUS = (
    (0, "Draft"),
    (0, "Publish"),
)

class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices= STATUS, default=0)
		
    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("aplicativo:detail", kwargs={"slug": self.slug})
