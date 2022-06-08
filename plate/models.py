from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
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
    
    following = models.ManyToManyField("self", symmetrical=False)
    
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
    
    
class Comment(models.Model):
    content = models.CharField(max_length=500, blank=False)
    
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    
    # 유저와 1 : N 관계
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 리뷰와 1 : N 관계
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.content[:30]
    

class Like(models.Model):
    dt_created = models.DateTimeField(auto_now_add=True)
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    
    object_id = models.PositiveIntegerField()
    
    liked_object = GenericForeignKey("content_type", "object_id")
    
    def __str__(self):
        return f"({self.user}, {self.liked_object})"
    