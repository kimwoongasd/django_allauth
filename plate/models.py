from turtle import update
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import BooleanField
from .validators import validate_no_special_characters, validate_store_link

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=15, 
                                unique=True, 
                                null=True,
                                validators=[validate_no_special_characters],
                                error_messages={"unique": "이미 사용중인 닉네임 입니다"},
                                )
    
    # 프로필 사진
    profile_pic = models.ImageField(default="default_profile_pic.jpg", upload_to="profile_pics")
    
    intro = models.CharField(max_length=60, blank=True)
    
    def __str__(self):
        return self.email
    
class Review(models.Model):
    title = models.CharField(max_length=30)
    store_name = models.CharField(max_length=20)
    store_link = models.URLField(validators=[validate_store_link])
    RATING_CHOICE = [
        (1, "★"),
        (2, "★★"),
        (3, "★★★"),
        (4, "★★★★"),
        (5, "★★★★★"),
    ]
    rating = models.IntegerField(choices=RATING_CHOICE, default=None)
    
    image_1 = models.ImageField(upload_to="review_pics")
    image_2 = models.ImageField(upload_to="review_pics", blank=True)
    image_3 = models.ImageField(upload_to="review_pics", blank=True)
    content = models.TextField()
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_modified = models.DateTimeField(auto_now=True)
    
    # 1 : N 관계
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
    