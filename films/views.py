from django.shortcuts import render

def films_list(request):
    return render(request,'films/films.html')
