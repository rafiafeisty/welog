from django.db import models
from django.contrib.auth.models import User
from signup.models import Signup
from django.utils.timezone import now  # Import for timezone-aware default

class Blogs(models.Model):
    blog_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True, blank=True)
    Titleblog = models.CharField(max_length=220, default="")
    content = models.CharField(max_length=720, default="")
    likes = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    image = models.ImageField(upload_to="allblog/images", default="")

    def __str__(self):
        return self.user.username

class Comments(models.Model):
    comment_id = models.AutoField
    user = models.ForeignKey(Signup, on_delete=models.CASCADE, null=True, blank=True)
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(default="")
    created_at = models.DateTimeField(default=now)  # Add created_at field

    def __str__(self):
        return self.user.username