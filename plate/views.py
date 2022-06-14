from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib.contenttypes.models import ContentType
from allauth.account.views import PasswordChangeView
from braces.views import LoginRequiredMixin
from plate.models import Review, User, Comment, Like
from .forms import ReviewForm, ProfileForm, CommentForm
from .mixins import LoginAndVerificationRequiredMixin, LoginAndOwnershipRequiredMixin

# Create your views here.
class IndexListView(ListView):
    model = Review
    template_name = "plate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    
class ReviewDetail(DetailView):
    model = Review
    template_name = "plate/review_detail.html"
    pk_url_kwarg = "review_id"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["review_ctype_id"] = ContentType.objects.get(model="review").id
        context["comment_ctype_id"] = ContentType.objects.get(model="comment").id
        return context
        
class ReviewCreate(LoginAndVerificationRequiredMixin, CreateView):
    model = Review
    template_name = "plate/review_form.html"
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

class ReviewUpdate(LoginAndOwnershipRequiredMixin, UpdateView):
    model = Review
    tmeplate_name = "plate/review_form.html"
    form_class = ReviewForm
    pk_url_kwarg = "review_id"

    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})
    
class ReviewDelete(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Review
    template_name = "plate/review_confirm_delete.html"
    pk_url_kwarg = "review_id"

    def get_success_url(self):
        return reverse("index")
    
    
# 유저 프로필
class ProfileView(DetailView):
    model = User
    template_name = "plate/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        context["user_reviews"] = Review.objects.filter(author__id=user_id)[:4]
        return context
    
class UserReviewListView(ListView):
    model = User
    template_name = "plate/user_review_list.html"
    context_object_name = "user_reviews"
    paginate_by = 4
    
    
    def get_queryset(self):
        user_id = self.kwargs.get("user_id")
        return Review.objects.filter(author__id=user_id)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile_user"] = get_object_or_404(User, id=self.kwargs.get("user_id"))
        return context

class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "plate/profile_set_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return  reverse("index")

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "plate/profile_update_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile", kwargs={"user_id": self.request.user.id})

class CommentCreateView(LoginAndVerificationRequiredMixin, CreateView):
    http_method_names = ["post"]
    model = Comment
    form_class = CommentForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.review = Review.objects.get(id=self.kwargs.get("review_id"))
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.kwargs.get("review_id")})

class CommentUpdateView(LoginAndOwnershipRequiredMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = "plate/comment_update_form.html"
    pk_url_kwarg = "comment_id"
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.review.id})
    
class CommentDeleteView(LoginAndOwnershipRequiredMixin, DeleteView):
    model = Comment
    template_name = "plate/comment_confirm_delete.html"
    pk_url_kwarg = "comment_id"

    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.review.id})

class ProcessLikeView(LoginAndVerificationRequiredMixin, View):
    http_method_names = ["post"]
    
    def post(self, request, *args, **kwargs):
        like, created = Like.objects.get_or_create(
            user = self.request.user,
            content_type_id = self.kwargs.get("content_type_id"),
            object_id = self.kwargs.get("object_id"),
        )

        if not created:
            like.delete()
            
        return redirect(self.request.META["HTTP_REFERER"])

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse("profile", kwargs={"user_id": self.request.user.id})
    
