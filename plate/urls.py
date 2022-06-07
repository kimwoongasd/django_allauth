from django.urls import path
from . import views

urlpatterns = [
    # review
    path('', views.IndexListView.as_view(), name="index"),
    path(
        "review/<int:review_id>/",
        views.ReviewDetail.as_view(),
        name="review-detail"
    ),
    path("review/new/", views.ReviewCreate.as_view(), name="review-create"),
    path("review/<int:review_id>/edit/", views.ReviewUpdate.as_view(), name="review-update"),
    path("review/<int:review_id>/delete/", views.ReviewDelete.as_view(), name="review-delete"),
    
    # profile
    path("uesrs/<int:user_id>/", views.ProfileView.as_view(), name="profile"),
    path("users/<int:user_id>/reviews/", views.UserReviewListView.as_view(), name="user-review-list"),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    
]