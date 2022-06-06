from django import forms
from .models import User, Review

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]
        
    def signup(self, request, user):
        user.nickname = self.cleaned_data["nickname"]
        user.save()
        
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
        