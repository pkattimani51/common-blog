from django.urls import path
from . import views


urlpatterns=[
	path('', views.blogs_index, name='blogs_index' ),
	path('<int:pk>/', views.blog_detail, name='blog_detail'),
	path('<category>/', views.blog_category, name='blog_category')
]