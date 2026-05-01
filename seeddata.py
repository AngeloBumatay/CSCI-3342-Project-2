from django.core.management.base import BaseCommand
from movies.models import *

class Command(BaseCommand):
    help = 'Load sample movie database records for Project 2.'

    def handle(self, *args, **kwargs):
        Slider.objects.all().delete(); MovieTheater.objects.all().delete(); MovieTV.objects.all().delete()
        Advertisement.objects.all().delete(); Celebrity.objects.all().delete(); Trailer.objects.all().delete()
        TrailerItem.objects.all().delete(); News.objects.all().delete(); Tweet.objects.all().delete(); SocialLink.objects.all().delete()

        for i, title in enumerate(['Interstellar','The Revenant','Die Hard','The Walk'], start=1):
            Slider.objects.create(image_src=f'images/uploads/slider{i}.jpg', image_width=285, image_height=437, anchor_url='#', movie_genre='Action', movie_title=title[:20], lower_rating='7.4', upper_rating='/10')

        movie_data = [
            ('Popular','images/uploads/mv-item1.jpg','Interstellar','Sci-Fi'),('Coming Soon','images/uploads/mv-item2.jpg','The Revenant','Action'),
            ('Top Rated','images/uploads/mv-item3.jpg','Die Hard','Action'),('Most Reviewed','images/uploads/mv-item4.jpg','The Walk','Adventure'),
            ('Popular','images/uploads/mv-item5.jpg','Oblivion','Sci-Fi'),('Coming Soon','images/uploads/mv-item6.jpg','Skyfall','Action'),
        ]
        for typ,img,title,genre in movie_data:
            MovieTheater.objects.create(type=typ,img_src=img,img_width=185,img_height=284,anchor_url='#',movie_genre=genre[:10],movie_title=title[:20],lower_rating='7.4',upper_rating='/10')
        for typ,img,title,genre in movie_data[:4]:
            MovieTV.objects.create(type=typ,img_src=img,img_width=185,img_height=284,anchor_url='#',movie_genre=genre[:10],movie_title=title[:20],lower_rating='7.0',upper_rating='/10')

        Advertisement.objects.create(section='homepage', img_src='images/uploads/ads1.png', img_width=336, img_height=296)
        Advertisement.objects.create(section='news', img_src='images/uploads/ads2.png', img_width=728, img_height=106)

        SocialLink.objects.create(name='Facebook', anchor_class='fb', icon_class='fa-facebook', url='#')
        SocialLink.objects.create(name='Twitter', anchor_class='tw', icon_class='fa-twitter', url='#')
        SocialLink.objects.create(name='Instagram', anchor_class='ig', icon_class='fa-instagram', url='#')

        Celebrity.objects.create(anchor_url='#', celebrity_url='images/uploads/ava1.jpg', celebrity_name='Samuel L. Jack', celebrity_type='Actor')
        Celebrity.objects.create(anchor_url='#', celebrity_url='images/uploads/ava2.jpg', celebrity_name='Ryan Reynolds', celebrity_type='Actor')
        Celebrity.objects.create(anchor_url='#', celebrity_url='images/uploads/ava3.jpg', celebrity_name='Emma Stone', celebrity_type='Actress')

        Trailer.objects.create(trailer_url='https://www.youtube.com/embed/1Q8fG0TtVAY')
        trailer_items = [
            ('images/uploads/trailer2.jpg','Wonder Woman','2:30'),('images/uploads/trailer6.jpg','Oblivion Official Trailer','2:37'),
            ('images/uploads/trailer3.png','Exclusive Interview','2:34'),('images/uploads/trailer4.png','Director Interview','2:43'),
        ]
        for img,desc,dur in trailer_items:
            TrailerItem.objects.create(img_src=img,img_alt=desc,img_width=100,img_height=56,description=desc,duration=dur)

        News.objects.create(section='Latest', img_src='images/uploads/blog-it1.jpg', img_alt='news', img_width=170, img_height=250,
            title='Brie Larson to play first female white house candidate', content='Exclusive movie news and entertainment updates are displayed dynamically from the database.', time='13 hours ago')
        News.objects.create(section='More News', img_src='images/uploads/blog-it2.jpg', img_alt='news', img_width=170, img_height=250,
            title='New trailers released this week', content='Movie fans can view fresh trailers, ratings, and updates through this Django backend project.', time='1 day ago')

        Tweet.objects.create(content='Always remember: dynamic sections should come from the database, not hardcoded HTML.')
        Tweet.objects.create(content='Movie news, trailers, ratings, and social links are now controlled through Django admin.')
        self.stdout.write(self.style.SUCCESS('Sample data loaded successfully.'))
