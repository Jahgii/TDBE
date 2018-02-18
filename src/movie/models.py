from django.db import models
from django.utils.encoding import smart_text
from django.utils.text import slugify

from django.db.models.signals import post_save, pre_save

from .validators import validate_studio_capital

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
    studio =    models.CharField(max_length=120, validators=[validate_studio_capital])
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

def movie_model_post_save_receiver(sender, instance, created, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug = slugify(instance.name)
        instance.save()

def movie_model_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug and instance.name:
        instance.slug=slugify(instance.name)
        instance.save()

post_save.connect(movie_model_post_save_receiver, sender = Movie)
pre_save.connect(movie_model_pre_save_receiver, sender = Movie)
