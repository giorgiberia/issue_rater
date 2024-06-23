from django.urls import path
from . import views

urlpatterns = [
    # path('', views.issue_list_and_create, name='issue_list_and_create'),
    path('about/', views.about, name='about'),
    path('vote/<int:issue_id>/', views.vote_issue, name='vote_issue'),
]
