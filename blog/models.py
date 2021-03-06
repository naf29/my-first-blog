from django.db import models
from django.utils import timezone

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name="Category", default='Category', null=True, blank=True, on_delete=models.CASCADE)
    # content = HTMLField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['published_date',]


    def approved_comments(self):
        return self.comments.filter(approved_comment=True)




class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    # get access to comments in Post model
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
