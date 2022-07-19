from experiences.models import Employment


def experience_processor(request):
    experiences = Employment.objects.all().order_by('-start_date')
    return {
        'experiences': experiences
    }