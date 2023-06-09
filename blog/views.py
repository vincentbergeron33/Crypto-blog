from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post


class PostList(View):
    def get(self, request, *args, **kwargs):
        categories = ['Crypto News', 'Bitcoin', 'Exchange', 'Decentralize']
        all_posts = []
        for each_category in categories:
            category_posts = Post.objects.filter(categorie=each_category)[:4]
            all_posts.append({"category": each_category, "posts": category_posts})
        
        return render(request, "index.html", {
          "all_posts": all_posts,
        })

    # model = Post
    # queryset = Post.objects.filter(status=1).order_by('-created_on')
    # template_name = 'index.html'


class CategoryPosts(View):
     def get(self, request, category_name, *args, **kwargs):
        queryset = Post.objects.filter(categorie=category_name)
        return render(
            request,
            "category_posts.html",
            {
                "posts": queryset,
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
                "liked": liked
            },
        )
