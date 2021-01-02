from django.urls import path
from . import views



urlpatterns = [
    path('', views.CommentList.as_view(), name='list'),
    path('<int:comment_id>/', views.CommentDetails.as_view(), name='details'),
]