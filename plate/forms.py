from django import forms
from .models import User, Review, Comment

# class SignupForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["nickname"]
        
#     def signup(self, request, user):
#         user.nickname = self.cleaned_data["nickname"]
#         user.save()
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "store_name",
            "store_link",
            "rating",
            "image_1",
            "image_2",
            "image_3",
            "content",
        ]
        
        widgets = {
            "rating": forms.RadioSelect,
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_pic",
            "intro"
        ]
        
        widgets= {
            "intro": forms.Textarea,
        }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "content",
        ]
        
        widgets = {
            "content": forms.Textarea,
        }