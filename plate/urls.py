from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexListView.as_view(), name="index"),
    path(
        "reviews/<int:review_id>",
        views.ReviewDetail.as_view(),
        name="review-detail"
    )
]