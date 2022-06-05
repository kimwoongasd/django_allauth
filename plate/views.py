from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from allauth.account.views import PasswordChangeView
from braces.views import LoginRequiredMixin
from plate.models import Review
from .forms import ReviewForm

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
    
class ReviewCreate(LoginRequiredMixin, CreateView):
    model = Review
    template_name = "plate/review_form.html"
    form_class = ReviewForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

class ReviewUpdate(UpdateView):
    model = Review
    tmeplate_name = "plate/review_form.html"
    form_class = ReviewForm
    pk_url_kwarg = "review_id"
    
    def get_success_url(self):
        return reverse("review-detail", kwargs={"review_id":self.object.id})

class ReviewDelete(DeleteView):
    model = Review
    template_name = "plate/review_confirm_delete.html"
    pk_url_kwarg = "review_id"
    
    def get_success_url(self):
        return reverse("index")

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
    
