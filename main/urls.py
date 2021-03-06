from django.urls import path
from . import views
urlpatterns = [
    path('', views.title),
    path('story/invasion', views.invasion),
    path('story/amulet', views.amulet),
    path('story/hammer', views.hammer),
    path('story/dragon', views.dragon),
    path('story/angus', views.angus),
    path('story/crail', views.crail),
    path('story/epic_rage', views.epic_rage),
    path('story/unicorn/redirect_unicorns', views.redirect_unicorns),
    path('story/unicorn/fight', views.fight_unicorn),
    path('story/unicorn/flee', views.flee_unicorn),
    path('story/unicorn/princess', views.princess_unicorn),
    path('battle/unicorn', views.unicorn_battle_page),
    path('battle/victory_unicorn', views.victory_unicorn),
    path('battle/death_unicorn', views.death_unicorn),
    path('princess/one', views.princess_one),
    path('princess/two', views.princess_two),
    path("princess/three", views.princess_three),
    path('death/one', views.death_one),
    path('kitchen/one', views.kitchen_one),
    path('stealth/check', views.stealth),
    path('kitchen/bread', views.bread),
    path('story/prologue', views.prologue),
    path('death/stealing', views.death_stealing),
    path('kitchen/cake', views.cake),
    path('kitchen/steak', views.steak),

]   