from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Category(models.Model):
    name = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.name

class CategoryImg(models.Model):
    imgName = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.imgName

class Post(models.Model):
    cat_id = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True)
    shorttext = models.CharField(max_length=150, null=True)
    text = RichTextUploadingField(null=True)
    date = models.DateField(null=True,)
    time = models.DateTimeField(null=True, auto_now_add=True, )
    img = models.ImageField(null=True)
    view_count = models.IntegerField(default=0, null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title

class PostImg(models.Model):
    cat_id = models.ForeignKey(CategoryImg, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200, null=True)
    img = models.ImageField(null=True)


    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title

class Comment(models.Model):
    title = models.CharField(max_length=200, null=True)
    text = RichTextUploadingField(null=True)
    time = models.DateTimeField(null=True, auto_now_add=True)
    img = models.ImageField(null=True)

    @property
    def get_image(self):
        try:
            return self.img.url
        except:
            return ""

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255,  blank=True)
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name