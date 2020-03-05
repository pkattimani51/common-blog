from django.shortcuts import render
from blogs.models import Category, Post, Comment
from .forms import CommentForm
# Create your views here.


def blogs_index(request):
	posts = Post.objects.all().order_by('-created_on')
	context = {'posts' : posts}
	return render(request, 'blogs_index.html', context)

def blog_category(request, category):
	posts = Post.objects.filter(
			categories__name__contains = category
		).order_by('-created_on')
	context = {
		'posts' : posts,
		'category' : category
	}
	return render(request, 'blog_category.html', context)



def blog_detail(request, pk):
	post = Post.objects.get(pk=pk)

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
					author = form.cleaned_data["author"],
					body = form.cleaned_data["body"],
					post = post
				)
			comment.save()
	form = CommentForm()
	comments = Comment.objects.filter(post=post)
	context = {
		'post' : post,
		'comments' : comments,
		'form' : form
	}
	return render(request, 'blog_detail.html', context)