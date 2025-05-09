from django import template
from ..models import Post

# Each module that contains template tags need to define a variable called register
# this variable is an instance of the Library class used to register template tags
# and filters to the applications
register = template.Library()


@register.simple_tag
# This tag (registered as a simple_tag which returns a string) returns the number
# of posts published in the blog
def total_posts():
    return Post.published.count()
