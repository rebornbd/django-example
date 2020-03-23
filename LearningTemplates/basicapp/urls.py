from django.conf.urls import url
from . import views

# TEMPLATE TAGGING
app_name = 'app_custom_name'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'other/', views.other, name='other'),
    url(r'relative/', views.relative, name='relative'),
]