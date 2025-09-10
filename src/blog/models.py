from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator



class Tag(models.Model):  
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Author(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100) 
    email = models.EmailField() 

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags = models.ManyToManyField(Tag)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_image/")
    date = models.DateField(auto_now=True)
    content = models.TextField(validators= [MinLengthValidator(10)])
    slug = models.SlugField(unique=True, db_index=True)

    def __str__(self):
        return f"{self.title}, {self.author}"
