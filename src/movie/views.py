from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .models import Movie

import redis
r = redis.Redis (host='localhost', port=6379, db=0)

def sql_to_redis(request):
    m = Movie.manager.all()

    List_Movies = {'Movies':{}}

    for i in m:
        List_Movies['Movies'].update(
        {i.id: [i.name, i.year, i.studio, i.genre, i.active, i.created]}
        )

        #List_Movies.append(List_Movie)

    r.set('Movies', List_Movies)
    return redirect('/')

def home (request):
    context = {'Movies': r.get('Movies')}

    return render(request, 'index.html', context)
