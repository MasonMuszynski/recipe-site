from django.conf.urls import url

from . import views

app_name = 'userprofile'

urlpatterns = [
    # ex: /profile/
    #url(r'^$', views.index, name='index'),

    # ex: /recipe/username/
    # url(r'^(?P<recipe_id>[0-9]+)/$', views.recipe_detail, name='detail'),
]