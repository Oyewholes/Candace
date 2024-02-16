from django.db import models

# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50, null=True, default='Random')
    
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author= models.CharField(max_length=30)
    image=models.ImageField(default="default_image.jpg", upload_to='blog_pics/')
    category=models.ForeignKey( Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name= models.CharField(max_length=30)
    email= models.EmailField()
    body= models.TextField()
    created_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post.title}'
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.email