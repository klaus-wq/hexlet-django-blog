# hexlet_django_blog/views.py
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = ["обучение", "программирование", "python", "oop"]
        return context

def index(request):
    return redirect('article', tags='python', article_id=42)

# def index(request):
#     return render(
#         request,
#         "index.html",
#         context={
#             "who": "World",
#         },
#     )

def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )