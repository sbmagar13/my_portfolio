from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse
from works.models import Work, Category_work
from django.views.generic import ListView
from django.db.models import Q
   
# Create your views here.

def work_index(request):
    works = Work.objects.filter(status=1).order_by('-created_on')
   
    

    paginator = Paginator(works, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
    }
    return render(request, "work_index.html", context)



def work_category(request, category_work):
    works = Work.objects.filter(
        categories__name__contains=category_work
    ).order_by(
        '-created_on'
    )
    
    paginator = Paginator(works, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "category_work": category_work,
         "page_obj": page_obj,
    }
    return render(request, "work_category.html", context)


def work_detail(request, pk):
    
    work = Work.objects.get(pk=pk)
    
    work.visit_num += 1
    work.save()
    
    '''
    comments = post.comments.filter(active=True, parent__isnull=True)
    if request.method == 'POST':
        # comment has been added
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj = None
            # get parent comment id from hidden input
            try:
                # id integer e.g. 15
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            # if parent_id has been submitted get parent_obj id
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                # if parent object exist
                if parent_obj:
                    # create replay comment object
                    replay_comment = comment_form.save(commit=False)
                    # assign parent_obj to replay comment
                    replay_comment.parent = parent_obj
            # normal comment
            # create comment object but do not save to database
            new_comment = comment_form.save(commit=False)
            # assign ship to the comment
            new_comment.post = post
            # save
            new_comment.save()
            return HttpResponseRedirect(reverse('blog_detail', args=(post.pk,)))
    else:
        comment_form = CommentForm()
    
    '''
    
    context = {
        "work": work,
    }

    return render(request, "work_detail.html", context)