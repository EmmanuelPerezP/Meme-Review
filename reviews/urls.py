"""
This file was created
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.MemeReviews.as_view(), name="meme_review_view")
]
