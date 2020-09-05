from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.CommentList.as_view(), name='list'),
    path('<int:comment_id>/', views.CommentDetails.as_view(), name='details'),
]