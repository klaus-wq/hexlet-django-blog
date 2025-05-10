from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexView, ArticleView, ArticleFormCreateView, ArticleFormEditView, \
    ArticleFormDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name='articles'),
    path("<int:id>/edit/", ArticleFormEditView.as_view(), name="articles_update"),
    path("<int:id>/delete/", ArticleFormDeleteView.as_view(), name="articles_delete"),
    path('<str:tags>/<int:article_id>/', views.index, name='article'),
    path("<int:id>/", ArticleView.as_view(), name='article_id'),
    path("create/", ArticleFormCreateView.as_view(), name="articles_create"),
]