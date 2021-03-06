from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30)
    
    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    category = models.ManyToManyField(Category)
    pub_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})
    

class Comment(models.Model):
    username = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['created_at']
        
    def __str__(self):
        return f'Comment by {self.username} on {self.article}'

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    liked = models.BooleanField(default=True)



# class Tag(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     name = models.CharField(max_length=30)