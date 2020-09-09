from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    published = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published = timezone.now()
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved=True)

    def get_absolute_url(self,*args,**kwargs):
        return reverse('my_app:post_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post,related_name='comment',on_delete=models.CASCADE)
    author = models.CharField(max_length=256,null=True,blank=True)
    text = models.TextField()
    created = models.DateTimeField(timezone.now())
    aprroved = models.BooleanField(default=False)

    def approved(self):
        self.approved=True
        self.save()

    def __str__(self):
        return self.text
