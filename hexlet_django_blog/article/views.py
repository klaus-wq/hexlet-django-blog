# hexlet_django_blog/article/views.py
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from hexlet_django_blog.article.forms import ArticleForm
from hexlet_django_blog.article.models import Article
from django.contrib import messages

class ArticleFormDeleteView(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.add_message(request, messages.ERROR, "Успешно удалено!")
        messages.add_message(request, messages.ERROR, "Ошибка при удалении!")
        return redirect("articles")

class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Успешно отредактировано!")
            return redirect("articles")
        messages.add_message(request, messages.ERROR, "Ошибка при редатировании!")
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid(): # Если данные корректные, то сохраняем данные формы
            form.save()
            messages.add_message(request, messages.SUCCESS, "Успешно создано!")
            return redirect('articles') # Редирект на указанный маршрут
        messages.add_message(request, messages.ERROR, "Ошибка при создании!")
        # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
        return render(request, 'articles/create.html', {'form': form})

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["id"])
        return render(
            request,
            "articles/show.html",
            context={
                "article": article,
            },
        )

class IndexView(View):
    # template_name = "articles/index.html"
#     #
#     # def get_context_data(self, **kwargs):
#     #     context = kwargs.copy()
#     #     context["app_name"] = "Hexlet Django Blog - Article"
#     #     return context
#     #
#     # def get(self, request, *args, **kwargs):
#     #     context = self.get_context_data(**kwargs)
#     #     return render(request, self.template_name, context)
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )

# def index(request):
#     context = {
#         'app_name': 'Hexlet Django Blog - Article'
#     }
#     return render(request, 'articles/index.html', context)

def index(request, tags, article_id):
    return HttpResponse(f'Статья номер {article_id}. Тег {tags}')