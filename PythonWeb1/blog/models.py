from django.db import models
from django.conf import settings

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=100)
    information = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True)
    def __str__(self):
        return self.name

class Comment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    