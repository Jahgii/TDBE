from django.db import models
from django.utils.encoding import smart_text
from django.utils.text import slugify

from django.db.models.signals import post_save, pre_save

from .validators import validate_studio_capital

from datetime import timedelta, datetime, date
from django.utils import timezone
from django.utils.timesince import timesince

# Create your models here.

GENRE_CHOICES = (
    ('action','Action'),
    ('adventure','Adventure'),
    ('comedy', 'Comedy'),
    ('drama','Drama'),
    ('horror','Horror'),
    ('war','War'),
    ('anime', 'Anime'),
)

class MovieModelQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active = True)
    def disabled(self):
        return self.filter(active= False)

class MovieModelManager(models.Manager):
    def get_queryset(self):
        return MovieModelQuerySet(self.model, using = self._db)

    def all(self, *args, **kwargs):
        qs = super(MovieModelManager,self).all(*args, **kwargs).filter(active = True)
        return (qs)

class Movie(models.Model):
    name        =   models.CharField(max_length=120, unique=True)
    year        =   models.CharField(max_length=120)
    studio      =   models.CharField(max_length=120, validators=[validate_studio_capital])
    genre       =   models.CharField(max_length=120, choices=GENRE_CHOICES)
    slug        =   models.SlugField(null=True, blank=True)
    active      =   models.BooleanField(default=True)
    created     =   models.DateField(auto_now=False, auto_now_add=False, default=timezone.now)
    update      =   models.DateTimeField (auto_now=True)
    timestamp   =   models.DateTimeField (auto_now_add=True)

    def __str__(self):
        return smart_text(self.name)

    def save (self, *args, **kwargs):
        if not self.slug:
            if self.name:
                self.slug = slugify (self.name)
        super (Movie, self).save(*args, **kwargs)

    @property
    def age(self):
        now = datetime.now()
        print (now)
        created_time = datetime.combine(self.created,
        datetime.now().max.time()
        )
        print (created_time)
        try:
            difference = now - created_time
            print (difference)
        except:
            return "Unknown"
        if difference <= timedelta(minutes=1):
            return "Right now"
        return '{time} ago'.format(time=timesince(created_time).split(', ')[0])

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
