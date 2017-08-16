from django.conf.urls import url

from . import views

app_name = 'recipe'
urlpatterns = [
    # ex: /explore/
    url(r'^$', views.explore, name='index'),

    # ex: /explore/add/
    url(r'^add/$', views.add_recipe, name='add'),

    # ex: /explore/5/
    url(r'^(?P<recipe_id>[0-9]+)/$', views.recipe_detail, name='detail'),
]