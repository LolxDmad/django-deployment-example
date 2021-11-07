from django.conf.urls import url,include
from . import views

app_name = 'basic_app'

urlpatterns= [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.relative,name='other')
]
