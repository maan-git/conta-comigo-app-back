from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from .models import Post


def index(request):
    latest_post_list = Post.objects.order_by()[:5]
    context = {
        'latest_post_list': latest_post_list,
    }
    return render(request, 'posts/index.html', context)


def help(request, post_id):
    try:
        post_selected = get_object_or_404(Post, pk=post_id)
        print("Post!")
        print(post_selected)
        # post_selected = post.get(pk=request.POST['post_id'])
    except (KeyError, Post.DoesNotExist):
        return render(request, 'posts/detail.html', {
            'post': post_selected,
            'error_message': "Error trying to help!",
        })
    else:
        post_selected.post_helps += 1
        post_selected.save()
        return render(request, 'posts/help_thank_you.html', {'post': post_selected})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/details.html', {'post': post})
