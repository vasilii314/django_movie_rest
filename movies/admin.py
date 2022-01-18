from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(MovieShots)
admin.site.register(Actor)
admin.site.register(Rating)
admin.site.register(RatingStar)
