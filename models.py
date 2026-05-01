from django.db import models

class Slider(models.Model):
    image_src = models.CharField(max_length=200)
    image_width = models.IntegerField(default=285)
    image_height = models.IntegerField(default=437)
    anchor_url = models.CharField(max_length=200, default='#')
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5, default='7')
    upper_rating = models.CharField(max_length=5, default='/10')
    def __str__(self): return self.movie_title

class Advertisement(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField(default=336)
    img_height = models.IntegerField(default=296)
    def __str__(self): return self.section

class SocialLink(models.Model):
    name = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=20, blank=True)
    icon_class = models.CharField(max_length=30)
    url = models.CharField(max_length=200)
    def __str__(self): return self.name

class Trailer(models.Model):
    trailer_url = models.CharField(max_length=200)
    def __str__(self): return self.trailer_url

class TrailerItem(models.Model):
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField(default=100)
    img_height = models.IntegerField(default=56)
    description = models.CharField(max_length=100)
    duration = models.CharField(max_length=10)
    def __str__(self): return self.description

class Celebrity(models.Model):
    anchor_url = models.CharField(max_length=200, default='#')
    img_width = models.IntegerField(default=70)
    img_height = models.IntegerField(default=70)
    celebrity_url = models.CharField(max_length=200)
    celebrity_name = models.CharField(max_length=50)
    celebrity_type = models.CharField(max_length=20)
    def __str__(self): return self.celebrity_name

class News(models.Model):
    section = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_alt = models.CharField(max_length=100)
    img_width = models.IntegerField(default=170)
    img_height = models.IntegerField(default=250)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    time = models.CharField(max_length=20)
    def __str__(self): return self.title

class Tweet(models.Model):
    content = models.TextField()
    def __str__(self): return self.content[:40]

class MovieTheater(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField(default=185)
    img_height = models.IntegerField(default=284)
    anchor_url = models.CharField(max_length=200, default='#')
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5, default='7')
    upper_rating = models.CharField(max_length=5, default='/10')
    def __str__(self): return self.movie_title

class MovieTV(models.Model):
    type = models.CharField(max_length=20)
    img_src = models.CharField(max_length=200)
    img_width = models.IntegerField(default=185)
    img_height = models.IntegerField(default=284)
    anchor_url = models.CharField(max_length=200, default='#')
    movie_genre = models.CharField(max_length=10)
    movie_title = models.CharField(max_length=20)
    lower_rating = models.CharField(max_length=5, default='7')
    upper_rating = models.CharField(max_length=5, default='/10')
    def __str__(self): return self.movie_title

class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.email
