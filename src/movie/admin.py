from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieModelAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'year',
        'studio',
        'genre',
        'slug',
        'active',
        'created',
        'update',
        'timestamp',
        'get_age'
    ]
    readonly_fields = ['created', 'update', 'timestamp', 'get_age']

    def get_age(self, obj, *args, **kwargs):
        return str(obj.age)

admin.site.register(Movie, MovieModelAdmin)
