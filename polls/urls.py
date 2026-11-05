from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("all", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("statistics", views.statistics, name="statistics"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]