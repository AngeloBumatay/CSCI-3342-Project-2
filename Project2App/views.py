from django.shortcuts import render
from .models import SocialLink, Slider, MovieTheater, Celebrity, Advertisement, MovieTV, TrailerItem, News, Trailer, Tweet

# Create your views here.
def index(request):
    social_links_data = SocialLink.objects.all()
    slider_data = Slider.objects.all()
    theater_data = MovieTheater.objects.all()
    celebrity_data = Celebrity.objects.all()
    advertisement_data = Advertisement.objects.all()
    tv_data = MovieTV.objects.all()
    trailer_data = Trailer.objects.all()
    trailer_item_data = TrailerItem.objects.all()
    news_data = News.objects.all()
    tweet_data = Tweet.objects.all()

    context = {
        'social_links': social_links_data,
        'slider_data': slider_data,
        'theater_data': theater_data,
        'celebrity_data': celebrity_data,
        'advertisement_data': advertisement_data,
        'tv_data': MovieTV.objects.all(),
        'trailer_data': Trailer.objects.all(),
        'trailer_item_data': TrailerItem.objects.all(),
        'news_data': News.objects.all(),
        'tweet_data': Tweet.objects.all()
    }

    return render(request, 'index.html', context)