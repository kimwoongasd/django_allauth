from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Review

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Review)

# 유저 모멜의 추가필드는 기본적으로 admin페이지에 나타나지 않기 떄문에 추가
# Custom fields라는 섹션아래에 nickname field를 추가
UserAdmin.fieldsets += (("Custom fields", {"fields" : ("nickname", "profile_pic", "intro")}),)

