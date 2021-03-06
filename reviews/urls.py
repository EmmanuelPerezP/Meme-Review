"""
This file was created
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.MemeReviews.as_view(), name="meme_review_view"),
    path("<int:pk>/", views.MemeDetail.as_view(), name="meme-detail"),
    path("<int:id>/<slug:slug>/", views.MemeDetail.as_view(),
         name="meme-detail"),
]
