from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            if form["text"] and form["title"]:
                posts = Article.objects.all()
                for i in posts:
                    if form["title"]==i.title:
                        form['errors'] = u"Такое название статьи уже есть. Придумайте другое"
                        return render(request, 'create_post.html', {'form': form})
                Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                post = Article.objects.get(title=form["title"])
                return redirect('get_article', article_id = post.id)
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404
