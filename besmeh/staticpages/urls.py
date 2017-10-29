from django.conf.urls import url

from .views import index, homepage_view, about_view

urlpatterns = [
	url(r'^$', index, name = "index_page"),
	url(r'^home/', homepage_view, name = "homepage"),
	url(r'^about/', about_view.as_view(), name = "about"),
]


