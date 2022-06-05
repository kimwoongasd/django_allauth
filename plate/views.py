from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from allauth.account.views import PasswordChangeView
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from allauth.account.models import EmailAddress
from plate.models import Review
from .forms import ReviewForm
from .functions import confirmation_required_redirect

# Create your views here.
class IndexListView(ListView):
    model = Review
    template_name = "plate/index.html"
    context_object_name = "reviews"
    paginate_by = 4
    ordering = ["-dt_created"]
    
class ReviewDetail(DetailView):
    model = Review
    template_name = "plate/review_detail.html"
    pk_url_kwarg = "review_id"
    
class ReviewCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Review
    template_name = "plate/review_form.html"
    form_class = ReviewForm
    
    redirect_unauthenticated_users = True
    raise_exception = confirmation_required_redirect
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

    def test_func(self, user):
        return EmailAddress.objects.filter(user=user, verified=True).exists()
   
class ReviewUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Review
    tmeplate_name = "plate/review_form.html"
    form_class = ReviewForm
    pk_url_kwarg = "review_id"
    
    raise_exception = True
    redirect_unauthenticated_users = False
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

    def test_func(self, user):
        review = self.get_object()
        return review.author == user

    
    
class ReviewDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Review
    template_name = "plate/review_confirm_delete.html"
    pk_url_kwarg = "review_id"
    
    raise_exception = True
    redirect_unauthenticated_users = False
    
    def get_success_url(self):
        return reverse("index")
    
    def test_func(self, user):
        review = self.get_object()
        return review.author == user

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
    
