from django import template
from ..models import Post
from django.db.models import Count

# Each module that contains template tags need to define a variable called register
# this variable is an instance of the Library class used to register template tags
# and filters to the applications
register = template.Library()


@register.simple_tag
# This tag (registered as a simple_tag which returns a string) returns the number
# of posts published in the blog
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
# This tag (registered as an inclusion tag which returns a dictionary of values) returns the latest 5 published posts
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
# This tag will return the most commented published posts
# returns a QuerySet using the annotate() method which aggregate the total number of comments for each post
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]
