from django.db import models
from django.utils.encoding import smart_text
from django.utils.text import slugify

# Create your models here.

GENRE_CHOICES = (
    ('action','Action'),
    ('adventure','Adventure'),
    ('comedy', 'Comedy'),
    ('drama','Drama'),
    ('horror','Horror'),
    ('war','War'),
)

class Movie(models.Model):
    name =      models.CharField(max_length=120, unique=True)
    year =      models.CharField(max_length=120)
    studio =    models.CharField(max_length=120)
    genre =     models.CharField(max_length=120, choices=GENRE_CHOICES)
    slug =      models.SlugField(null=True, blank=True)
    active =    models.BooleanField(default=True)
    created =   models.DateField(auto_now=True)
    update =    models.DateTimeField (auto_now=True)
    timestamp = models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return smart_text(self.name)

    def save (self, *args, **kwargs):
        if not self.slug:
            if self.name:
                self.slug = slugify (self.name)
        super (Movie, self).save(*args, **kwargs)
