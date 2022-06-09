from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import User, Review, Comment, Like

# Register your models here.


class CommentInlinme(admin.StackedInline):
    model = Comment
    

class LikeInlinme(GenericStackedInline):
    model = Like   

class UserInline(admin.StackedInline):
    model = User.following.through
    fk_name = "to_user"
    verbose_name = "Follower"
    verbose_name_plural = "Followers"
    

class ReviewAdmin(admin.ModelAdmin):
    inlines = (
        CommentInlinme,
        LikeInlinme,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInlinme,
    )

admin.site.register(User, UserAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like)  

# 유저 모멜의 추가필드는 기본적으로 admin페이지에 나타나지 않기 떄문에 추가
# Custom fields라는 섹션아래에 nickname field를 추가
UserAdmin.fieldsets += (("Custom fields", {"fields" : ("nickname", "profile_pic", "intro", "following")}),)
UserAdmin.inlines = (UserInline,)
