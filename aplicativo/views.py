
from django.views.generic import DetailView, ListView
from django.template import RequestContext
from django.shortcuts import get_list_or_404, get_object_or_404, render
from .forms import CommentForm
from .models import Post


from aplicativo.formulario import Comment


class PostListView(ListView):
    model = Post


#class PostDetailView(DetailView):
#   model = Post


def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by('created')
    new_comment = None

    if request.method == 'Post':
        comment_form = CommentForm(data=request.Post)
        if comment_form.is_valid():

            new_comment = comment_form.save(commit=True)

            new_comment.post = post

            new_comment.save()

    else:
        comment_form = CommentForm()

    return render (
        request,
        template_name,
        {
            'post': post,
            'comments': comments,
            'new_comment': new_comment,
            'comment_form': comment_form,
        },
    )

