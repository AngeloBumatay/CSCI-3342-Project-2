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

def movie_single(request, movie_id):
    specific_movie = get_object_or_404(MovieTheater, id=movie_id)
    
    context = {
        'movie': specific_movie,
    }
    
    return render(request, 'moviesingle.html', context)