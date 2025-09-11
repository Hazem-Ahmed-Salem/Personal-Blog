from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator



class Tag(models.Model):  
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    

class Author(models.Model):
    user  = models.OneToOneField("auth.User",null=True, on_delete=models.CASCADE,related_name="author")
    bio   = models.CharField(null=True,max_length=200) 
    about = models.TextField(null=True,)
    what_i_do = models.TextField(null=True,max_length=300) 
    def __str__(self):
        return self.user.get_full_name()

class Link(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(null=True,max_length=50)
    link = models.URLField()
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=150)
    author = models.ForeignKey(Author,on_delete=models.SET_NULL,related_name="posts",null=True)
    tags = models.ManyToManyField(Tag)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="post_image/")
    date = models.DateField(auto_now=True)
    content = models.TextField(validators= [MinLengthValidator(10)])
    slug = models.SlugField(unique=True, db_index=True)
    links = models.ManyToManyField(Link,null=True,blank=True,related_name='links') 

    def __str__(self):
        return f"{self.title}, {self.author}"


class Comment(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField()
    text = models.TextField(max_length=500)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}: {self.text[:] if (len(self.text) <= 20) else self.text[:20]+" ...."}"
    
