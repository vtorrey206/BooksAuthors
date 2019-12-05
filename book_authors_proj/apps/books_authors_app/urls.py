from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_book$', views.process_book),
    url(r'^description/(?P<id>\d+)$', views.description),
    url(r'^push_author/(?P<book_id>\d+)$', views.push_author),
    url(r'^author$', views.author),
    url(r'^process_author$', views.process_author),
    url(r'^notes/(?P<id>\d+)$', views.notes),
    url(r'^push_book/(?P<author_id>\d+)$', views.push_book),
    
    
    
]