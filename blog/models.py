from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# The below will allow the superuser to create draft posts

STATUS = ((0, "Draft"), (1, "Published"))

# This value will be insert in the database struture as a categorie

CATEGORIE_CHOICES = (
   ('Crypto News', 'Crypto News'),
   ('Bitcoin', 'Bitcoin'),
   ('Exchange', 'Exchange'),
   ('Decentralize', 'Decentralize'),
)

# Create the database structure of the posts


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    categorie = models.CharField(choices=CATEGORIE_CHOICES, max_length=128)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

# Create the database structure of the comments


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

# Create the database structure of the scams


class Scam(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=200, unique=True)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    media = models.CharField(max_length=80)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
