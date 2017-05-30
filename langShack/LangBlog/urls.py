from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [ 
	url(r'^$', ListView.as_view(
	                    queryset=Post.objects.all().order_by("-created_at")[:25],
	                    template_name="langblog.html")),
]