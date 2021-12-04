from django.shortcuts import render

def index(request):
    context = {
    "online" : range(100,1000) 
}
    return render(request, 'index.html', context)

def error_404(request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def animes(request):
    return render(request, 'animes.html')

def books(request):
    return render(request, 'books.html')

def games(request):
    return render(request, 'games.html')

def home(request):
    return render(request, 'home.html')

def movies(request):
    return render(request, 'movies.html')

def profile(request):
    return render(request, 'profile.html')

def series(request):
    return render(request, 'series.html')

def work(request):
    return render(request, 'work.html')

