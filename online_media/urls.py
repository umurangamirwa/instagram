from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    
    url('^$',views.index, name='index'),
    url(r'^$',views.profile,name = 'profile'),
    # url(r'^comment/(?P<id>\d+)', views.comment, name='comment'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^upload/images', views.upload_images, name='upload_images'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^upload/profile', views.upload_profile, name='upload_profile'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 
    urlpatterns+= static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
