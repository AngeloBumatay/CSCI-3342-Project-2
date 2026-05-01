from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def home(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            NewsletterSubscriber.objects.get_or_create(email=email)
            messages.success(request, 'Thank you for subscribing!')
        return redirect('home')

    context = {
        'sliders': Slider.objects.all(),
        'movies_theater': MovieTheater.objects.all(),
        'movies_tv': MovieTV.objects.all(),
        'ads': Advertisement.objects.all(),
        'social_links': SocialLink.objects.all(),
        'celebrities': Celebrity.objects.all(),
        'trailers': Trailer.objects.all(),
        'trailer_items': TrailerItem.objects.all(),
        'news_items': News.objects.all(),
        'tweets': Tweet.objects.all(),
    }
    return render(request, 'movies/home.html', context)
