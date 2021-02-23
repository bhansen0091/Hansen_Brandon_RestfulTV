from django.shortcuts import render, redirect
from restful_tv_app.models import TVShow

def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        "tv_shows": TVShow.objects.all()
    }
    return render(request, "shows.html", context)

def new_show(request):

    return render(request, "new_show.html")