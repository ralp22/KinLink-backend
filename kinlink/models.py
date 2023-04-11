from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserImageSelection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_selections')

    def __str__(self):
        return self.image.name


class Relationship(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
    relationship_type = models.CharField(max_length=100)

class UserProfile(User):
    # class Meta:
    #     proxy = True

    avatar = models.ImageField(upload_to='avatars/', blank=True)
    highlight_reel = models.ManyToManyField(UserImageSelection, blank=True, max_length=10)
    relationships = models.ManyToManyField(Relationship, blank=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}"
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.content[:50]}"
    

# user = request.user
# profile = user.userprofile
# avatar = profile.avatar
    
# Comment model has a Fkey to both the UserProfile and Post models. The related_name argument in the post field of the Comment model allows access all the comments for a particular post via post.comments.all()

# **kwargs is a special syntax in Python for passing a keyworded, variable-length argument list to a function. The term "kwargs" stands for keyword arguments.

# In Python, you can use **kwargs to pass a dictionary of keyword arguments to a function. This allows you to pass any number of keyword arguments to the function, without having to specify them all in the function definition.
