from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator
import os
import datetime


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.category_name}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    caption = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.caption}"


def filepath(request, filename):
    old_filename = filename
    timenow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (timenow, old_filename)
    return os.path.join('uploads/', filename)


# Author and Post one-to-many relation
class Post(models.Model):
    post_title = models.CharField(max_length=100,null=True)
    post_content = models.TextField(validators=[MinLengthValidator(10)], null=True)
    post_image = models.ImageField(upload_to=filepath)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="posts")
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.post_title}"


# post and comment One-to-Many relation
class Comment(models.Model):
    comment_content = models.CharField(max_length=200)
    comment_date = models.DateField(auto_now=True)
    username = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,  related_name='comments')

    def __str__(self):
        return f"{self.comment_content}"
