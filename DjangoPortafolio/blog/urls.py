from django.urls import path
from .views import posts, post_detail

app_name= "blog"

urlpatterns=[
    path('', posts, name='posts'),
    path('<int:post_id>', post_detail, name="post_detail"),

]