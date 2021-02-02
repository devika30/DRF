from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    date=models.DateTimeField(max_length=100,null=True,blank=True,auto_now_add=True)

    def __str__(self):
        return self.title
