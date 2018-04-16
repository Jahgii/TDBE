from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect
from .models import Movie

import redis
r = redis.Redis (host='localhost', port=6379, db=0)

def sql_to_redis(request):
    m = Movie.manager.all()

    List_Movies = []

    for i in m:
        List_Movie ={
        'Movies':{m.get(id=i.id).id: [m.get(id=i.id).name, m.get(id=i.id).year, m.get(id=i.id).studio, m.get(id=i.id).genre, m.get(id=i.id).active, m.get(id=i.id).created]}
        }

        List_Movies.append(List_Movie)

    r.set('Movies', List_Movies)
    return redirect('/')

def home (request):
    context = {'Movies': r.get('Movies')}

    return render(request, 'index.html', context)
