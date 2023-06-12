from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Post, Scam
from django.http import HttpResponseRedirect
from .forms import CommentForm


class PostList(View):
    def get(self, request, *args, **kwargs):
        categories = ['Crypto News', 'Bitcoin', 'Exchange', 'Decentralize']
        all_posts = []
        for each_category in categories:
            category_posts = Post.objects.filter(categorie=each_category)[:4]
            all_posts.append(
                {"category": each_category, "posts": category_posts})
       
        return render(request, "index.html", {
          "all_posts": all_posts,
        })


class ScamList(generic.ListView):
    def get(self, request, *args, **kwargs):
        model = Scam
        queryset = Scam.objects.order_by('-created_on')
        template_name = 'scam.html'

        return render(request, 'scam.html')


class CategoryPosts(View):
    def get(self, request, category_name, *args, **kwargs):
        queryset = Post.objects.filter(categorie=category_name)
        return render(
            request,
            "category_posts.html",
            {
                "posts": queryset,
                "categorie": category_name
            },
        )


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostScam(View):
    def get(self, request, *args, **kwargs):
        scams = Scam.objects.all()
        context = {
            'scams': scams
        }
        return render(request, 'report_scam.html', context)


def add_scam(request, *args, **kwargs):
    if request.method == 'POST':
        title = request.POST.get('scam_title')
        media = request.POST.get('scam_media')
        excerpt = request.POST.get('scam_excerpt')
        content = request.POST.get('scam_content')
        Scam.objects.create(
            title=title, media=media, excerpt=excerpt, content=content)

        return redirect('home')

    return render(request, 'report_scam.html')


class ScamDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Scam.objects.filter(status=1)
        scam = get_object_or_404(queryset, slug=slug)
        comments = scam.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        return render(
            request,
            "scam_detail.html",
            {
                "scam": scam,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        scam = get_object_or_404(queryset, slug=slug)
        comments = scam.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "scam_detail.html",
            {
                "scam": scam,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )