from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns =[
  url('^$',views.home,name='index'),
  url('^about',views.about,name='about'),
  url('^projects',views.projects,name='projects')
]
if settings.DEBUG:
  urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)