from django.urls import re_path as url
from . import views


urlpatterns =[
  url('^$',views.home,name='welcome'),
  url('^about',views.about,name='about'),
  url('^projects',views.projects,name='projects')
]