from django.shortcuts import render
from .models import Events, Announcer, Mentors, Trainers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404


# Create your views here.
def index(request):
    # mentors = Mentors.objects.all().order_by('-id')[0:][:3]
    events = Events.objects.all().order_by('-id')[0:][:3]

    context = {
        # 'mentors': mentors,
        'events': events
    }
    return render(request, 'index.html', context)

def about(request):
    announcer = Announcer.objects.all().order_by('-id')
    context = {
        'announcer': announcer
    }
    return render(request, 'about.html', context)

def events(request):
    events = Events.objects.all().order_by('-id')
    page_num = request.GET.get('page', 1)

    paginator = Paginator(events, 6) # 6 employees per page

    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        # if page is not an integer, deliver the first page
        page_obj = paginator.page(1)
    except EmptyPage:
        # if the page is out of range, deliver the last page
        page_obj = paginator.page(paginator.num_pages)

    context = {
        'events': page_obj.object_list,
        'page_obj': page_obj
    }
    return render(request, 'events.html', context)

def event_detail(request, slug):
    events = get_object_or_404(Events, slug = slug)
    related_events = Events.objects.exclude(slug=events.slug).order_by('-id')[0:2]


    context = {
        'events' : events,
        'related_events' : related_events
    }

    return render(request, 'event-details.html', context)

def incubation(request):
    mentors = Mentors.objects.all().order_by('-id')
    trainers = Trainers.objects.all().order_by('-id')

    context = {
        'mentors': mentors,
        'trainers': trainers

    }
    return render(request, 'incubation-program.html', context)