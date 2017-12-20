from django.shortcuts import render
from django.views import generic, View
from .models import Image, Meme, Review
from .forms import CreateReview
from django.views.generic.edit import SingleObjectMixin, FormView
# from django.utils import slugify
from django.urls import reverse


# generic.ListView automatically gets the "context" the context is the data
# passed to the template like a dictionary {memes: meme} in this case
# all the memes
class MemeReviews(generic.ListView):
    model = Meme
    context_object_name = "meme_list"
    template_name = "index.html"
    paginate_by = 3
    ordering = ['-dateCreated']


# to have the meme review form in MemeDetailview we seperate the 2 reviews
# into MemeDisplay and MemeReviewFormView using mixins
class MemeDisplay(generic.DetailView):
    model = Meme

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateReview()
        return context


class MemeReviewFormView(SingleObjectMixin, FormView):
    """
    MemeReviewFormView is a simple FormView, but we have to bring in
    SingleObjectMixin so we can find the meme we’re talking about, and we
    have to remember to set template_name to ensure that form errors will
    render the same template as MemeDisplay is using on GET
    """
    template_name = "reviews/meme_detail.html"
    form_class = CreateReview
    model = Meme

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        print("Meme name: " + str(self.object.title))
        return reverse('meme-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        reviewMo = Review(textReview=form.cleaned_data['message'],
                          titleReview="temp",
                          ratingReview=form.cleaned_data['rating'])
        reviewMo.save()
        self.object.reviews.add(reviewMo)
        return super().form_valid(form)


class MemeDetail(View):

    def get(self, request, *args, **kwargs):
        view = MemeDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = MemeReviewFormView.as_view()
        return view(request, *args, **kwargs)
