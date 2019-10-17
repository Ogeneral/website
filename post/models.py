from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    Your_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', auto_now_add=True)   
    Your_Post_title = models.CharField(max_length=200)  
    Your_Post = models.TextField(max_length=2000)
    id = models.IntegerField(primary_key=True)
    def __str__(self):
        return self.Your_Post


class Comment(models.Model):
    name = models.CharField(max_length=42)   
    text = models.TextField()
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text


 
