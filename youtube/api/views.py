from django.shortcuts import render
from django.http import HttpResponse
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.postgres.search import SearchQuery, SearchVector

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

def search_videos(request):
    if request.method == 'POST':
        query_list = request.POST.get('query')
        query_split_list = query_list.split(' ')
        a = "SearchQuery('"
        m='search='
        for query in  query_split_list:
            m = m + a + query + "') & "
        m = "models.Videos.objects.annotate(search=SearchVector('title', 'description')).filter(" + m[:-2] + ")"
        videos_queryset = eval(m)
        return render(request, 'video_display.html', {'videos':videos_queryset})
    else:
        return render(request, 'search.html')