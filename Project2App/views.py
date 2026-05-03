from django.shortcuts import render, redirect, get_object_or_404
from .models import SocialLink, Slider, MovieTheater, Celebrity, Advertisement, MovieTV, TrailerItem, News, Trailer, Tweet, Subscriber

# Create your views here.
def index(request):

    # Form submission 
    if request.method == 'POST':
        user_email = request.POST.get('email')
        if user_email:
            Subscriber.objects.get_or_create(email=user_email)
            return redirect('/')

    social_links_data = SocialLink.objects.all()
    slider_data = Slider.objects.all()
    celebrity_data = Celebrity.objects.all()
    sidebar_ads = Advertisement.objects.filter(section='Sidebar')
    news_ads = Advertisement.objects.filter(section='News')
    theater_popular = MovieTheater.objects.filter(type='Popular')
    theater_coming = MovieTheater.objects.filter(type='Coming Soon')
    tv_popular = MovieTV.objects.filter(type='Popular')
    tv_coming = MovieTV.objects.filter(type='Coming Soon')
    trailer_data = Trailer.objects.all()
    trailer_item_data = TrailerItem.objects.all()
    news_data = News.objects.all()
    tweet_data = Tweet.objects.all()

    context = {
        'social_links': social_links_data,
        'slider_data': slider_data,
        'theater_popular': theater_popular,
        'theater_coming': theater_coming,
        'tv_popular': tv_popular,
        'tv_coming': tv_coming,
        'celebrity_data': celebrity_data,
        'sidebar_ads': sidebar_ads,
        'news_ads': news_ads,
        'trailer_data': trailer_data,
        'trailer_item_data': trailer_item_data,
        'news_data': news_data,
        'tweet_data': tweet_data,
    }

    return render(request, 'index.html', context)

def movie_single(request, movie_id):
    return render(request, 'moviesingle.html')