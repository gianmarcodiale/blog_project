from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404
from django.views.generic import ListView


class PostListView(ListView):
    """
    Alternative post list view
    """
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    post_list = Post.published.all()
    # Pagination with 3 post per page
    paginator = Paginator(post_list, 3)
    # Retrieve the current page number
    page_number = request.GET.get('page', 1)
    # Get the current page posts
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page number is not an integer get the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page number is out of range get last page of results
        posts = paginator.page(paginator.num_pages)
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )


def post_detail(request, year, month, day, post):
    #    try:
    #        post = Post.published.get(id=id)
    #    except Post.DoesNotExist:
    #        raise Http404("No Post found.")
    post = get_object_or_404(
        Post,
        status=Post.Status.PUBLISHED,
        slug=post,
        publish__year=year,
        publish__month=month,
        publish__day=day
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )
