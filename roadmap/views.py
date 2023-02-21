from django.shortcuts import render

from roadmap.models import Roadmap, RoadmapTopic


def roadmap(request):
    roadmaps = Roadmap.objects.all()
    topics = RoadmapTopic.objects.all().order_by('priority')
    return render(request, "roadmap.html", {'roadmaps': roadmaps, 'topics': topics})
