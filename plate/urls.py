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
    path('reviews/', views.ReviewListView.as_view(), name='review-list'),
    path("review/new/", views.ReviewCreate.as_view(), name="review-create"),
    path("review/<int:review_id>/edit/", views.ReviewUpdate.as_view(), name="review-update"),
    path("review/<int:review_id>/delete/", views.ReviewDelete.as_view(), name="review-delete"),
    
    # profile
    path("uesrs/<int:user_id>/", views.ProfileView.as_view(), name="profile"),
    path("users/<int:user_id>/reviews/", views.UserReviewListView.as_view(), name="user-review-list"),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
    path("edit-profile/", views.ProfileUpdateView.as_view() , name="profile-update"),
    
    # comment
    path("review/<int:review_id>/comments/create/", views.CommentCreateView.as_view(), name="comment-create"),
    path("review/<int:comment_id>/comments/edit/", views.CommentUpdateView.as_view(), name="comment-update"),
    path("review/<int:comment_id>/comments/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
    
    # like
    path("like/<int:content_type_id>/<int:object_id>/", views.ProcessLikeView.as_view(), name="process-like"),
    
    #follow
    path("user/<int:user_id>/follow/", views.ProcessFollowView.as_view(), name="process-follow"),
    path('users/<int:user_id>/following/', views.FollowingListView.as_view(), name='following-list'),
    path('users/<int:user_id>/followers/', views.FollowerListView.as_view(), name='follower-list'),
    
]