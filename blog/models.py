from django.db import models
from django.contrib.auth.models import User


class AbstractModel(models.Model):
    object = None

    class Meta:
        abstract = True
        ordering = ['-updated_at']
        get_latest_by = 'updated_at'

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(User, related_name='+', blank=True, null=True, default=None,
                                   on_delete=models.SET_NULL, editable=False)
    updated_by = models.ForeignKey(User, related_name='+', blank=True, null=True, default=None,
                                   on_delete=models.SET_NULL, editable=False)


class Tweet(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True, default=None)
    description = models.TextField()
    likes = models.ManyToManyField(User,related_name='like')
    image = models.ImageField(blank=True, null=True, default=None, upload_to='tweet/image')

    def __str__(self):
        return self.title


class Comment(AbstractModel):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
