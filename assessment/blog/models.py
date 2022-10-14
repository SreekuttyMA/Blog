from email.policy import default
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# from blog.views import like_post

# Create your models here.
class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, default=None , blank=True,related_name='liked')
    class Meta:
        ordering =('-date_created',)
    
    def comment_count(self):
        return self.comment_set.all().count()
    
    def comments(self):
        return self.comment_set.all()
    
    
    def num_likes(self):
        return self.liked_set.all().count()
    
    def __str__(self):
        return self.title
    
LIKE_CHOICES =(
    ('Like','Like'),
    ('Unlike','Unlike'),
)   
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)
    
    def __str__(self):
        return self.value
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=150)

    def __str__(self):
        return self.content

