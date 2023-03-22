from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.test import tag
from .forms import CommentForm
from django.urls import reverse
from blogs.models import Post, Comment
from django.db.models import Q

import random
from taggit.models import Tag
from django.db.models import Count
from django.contrib import messages


def blog_index(request, tag_slug=None):
    posts = Post.objects.filter(status=1).order_by('-publish')

    tag=None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 15)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    # page_obj = paginator.get_page(page_number)

    context = {
        'page_number': page_number,
        'page_obj': page_obj,
        'tag': tag
    }
    return render(request, "blog_index.html", context)


########################################################################

def blog_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,
                                   status=1,
                                   publish__year=year,
                                   publish__month=month,
                                   publish__day=day)
    
    post.visit_num += 1
    post.save()

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
            messages.success(request, "Comment successfully posted!")

            return HttpResponseRedirect(reverse('blog_detail', args={year:post.publish.year,
                                                                     month:post.publish.month,
                                                                     day:post.publish.day,
                                                                     post:post.slug,
                                                                    }))
    
    else:
        comment_form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:3]
    
    context = {
        "post": post,
        "comments": comments,
        "comment_form": comment_form,
        "similar_posts": similar_posts
    }


    return render(request, "blog_detail.html", context)


########################################################################


def blog_category(request, category_post, tag_slug=None):
    posts = Post.objects.filter(
        categories__name__contains=category_post
    ).order_by(
        '-created_on'
    )

    tag=None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 9)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.page(page_number)

    except PageNotAnInteger:
        page_obj = paginator.page(1)

    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    context = {
        "category_post": category_post,
        "page_number": page_number,
        "page_obj": page_obj,
        "tag": tag,
    }
    return render(request, "blog_category.html", context)

