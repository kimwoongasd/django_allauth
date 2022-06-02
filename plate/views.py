from django.urls import reverse
from django.views.generic import ListView, DetailView
from allauth.account.views import PasswordChangeView
from plate.models import Review

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

class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
    
