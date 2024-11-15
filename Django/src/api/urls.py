from django.urls import path
from . import views

urlpatterns = [
    # POST http://localhost:8000/api/login
    path("login", views.log_in),

    # POST http://localhost:8000/api/logout
    path("logout", views.log_out),

    # GET http://localhost:8000/api/stats
    path("stats", views.get_vacations_stats),

    # GET http://localhost:8000/api/totalusers
    path("totalusers", views.get_total_users),

    # GET http://localhost:8000/api/totallikes
    path("totallikes", views.get_total_likes),

    # GET http://localhost:8000/api/likespercountry
    path("likespercountry", views.get_likes_split),

]