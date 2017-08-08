from django.conf.urls import url

from . import views

app_name = 'recipe'
urlpatterns = [
    # ex: /recipe/
    url(r'^$', views.index, name='index'),

    # ex: /recipe/5/
    # url(r'^(?P<recipe_id>[0-9]+)/$', views.detail, name='detail'),
]