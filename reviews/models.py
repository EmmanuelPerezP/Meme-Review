from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Image(models.Model):
    imageURL = models.URLField()

    def __str__(self):
        return self.imageURL


class Meme(models.Model):
    mainImage = models.ForeignKey('Image', on_delete=models.SET_NULL,
                                  null=True,
                                  related_name='mainImage')
    relatedImages = models.ManyToManyField('Image',
                                           related_name='relatedImages')
    reviews = models.ManyToManyField('Review')
    description = models.CharField(max_length=1000)
    title = models.CharField(max_length=300)
    dateCreated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=300)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        return the url to access this particular post
        """
        return reverse('meme-detail', args=[self.id, slugify(self.title)])


class Review(models.Model):
    textReview = models.CharField(max_length=300)
    titleReview = models.CharField(max_length=100)
    ratingReview = models.IntegerField()

    def __str__(self):
        return self.titleReview
