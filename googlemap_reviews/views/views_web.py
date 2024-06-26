from django.shortcuts import render, HttpResponse,redirect
from googlemap_reviews import models


def googlemap_reviews(request):
    KeyWordReviews = models.KeyWordReviews.objects.all()
    return render(request,'googlemap_reviews.html')

# Create your views here.
