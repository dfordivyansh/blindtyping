from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("test/<int:test_id>/", views.take_test, name="take_test"),
    path("submit/", views.submit_result, name="submit_result"),
    path("leaderboard/", views.leaderboard, name="leaderboard"),
    path("rules/", views.rules, name="rules"),

]
