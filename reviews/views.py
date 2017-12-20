from django.shortcuts import render
from django.views import generic
from .models import Image, Meme, Review
from .forms import CreateReview
from django.views.generic.edit import FormMixin


# generic.ListView automatically gets the "context" the context is the data
# passed to the template like a dictionary {memes: meme} in this case
# all the memes
class MemeReviews(generic.ListView):
    model = Meme
    context_object_name = "meme_list"
    template_name = "index.html"
    paginate_by = 3
    ordering = ['-dateCreated']


class Meme(generic.DetailView, FormMixin):
    model = Meme
    form_class = CreateReview
