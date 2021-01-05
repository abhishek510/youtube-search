from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    video_list = models.Videos.objects.order_by('-published_date')
    page = request.GET.get('page', 1)

    paginator = Paginator(video_list, 10)

    try:
        videos = paginator.page(page)
    except PageNotAnInteger:
        videos = paginator.page(1)
    except EmptyPage:
        videos = paginator.page(paginator.num_pages)

    return render(request, 'video_display.html', {'videos':videos})