from django.conf.urls import url
from .views import hello,show
urlpatterns = [
    url(r'^$', hello),
    url(r'(?P<pk>[0-9]+)',show)
]
