from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
import random

def title(request):
    return render(request, "title.html")

def amulet(request):
    return render(request, "amulet_of_justic.html")

def hammer(request):
    return render(request, "Quest_for_the_hammer.html")

def dragon(request):
    return render(request, "magic_dragon.html")

def invasion(request):
    context = {
        'action': 0 , 
        "start": 1

    }
    return render(request, "The_Unicorn_Invasion.html", context)

def angus(request):
    return render(request, "Angus_McFife.html")

def crail(request):
    return render(request, "Hail_to_Crail.html")

def epic_rage(request):
    return render(request, "The_epic_rage.html")

def princess_unicorn(request):
    context = {
        "unicorn_choice" : 1,
        'action': 1
    }
    return render (request, "The_Unicorn_Invasion.html" ,context)

def flee_unicorn(request):
    context = {
        'unicorn_choice' : 2,
        'action': 2
    }
    return render (request, "The_Unicorn_Invasion.html", context)

def fight_unicorn(request):
    context = {
        'unicorn_choice': 3,
        'action': 3
    }
    return render(request, "The_Unicorn_Invasion.html", context)

def redirect_unicorns(request):
    return redirect('/story/invasion')

def unicorn_battle_page(request):
    if "angus_hp" not in request.session:
        request.session['angus_hp'] = 100
        request.session['angus_defense'] = 12
        request.session['combat_log']=[]
    if 'unicorn_hp' not in request.session:
        request.session['unicorn_hp'] = 50
        request.session['unicorn_defense'] = 10
    context = {
        'angus_hp': request.session['angus_hp'],
        'angus_defense' : request.session['angus_defense'],
        'unicorn_hp': request.session['unicorn_hp'],
        'unicorn_defense' : request.session['unicorn_defense'],
        'combat_log' : request.session['combat_log'],
        'angus_hp' : request.session['angus_hp'],
        'angus_hit' : random.randint(1, 20),
        'angus_dmg' : random.randint(5, 10),
        'unicorn_hp' : request.session['unicorn_hp'],
        'unicorn_hit' : random.randint(1, 20),
        'unicorn_dmg' :random.randint(1, 10)
    }
    return render (request, "battle/unicorn.html", context)

def victory_unicorn(request):
    return render (request, "victory_unicorn.html")

def death_unicorn(request):
    return render (request, "death_unicorn.html")

def princess_one(request):
    context = {
        'unicorn_choice': 1 ,
        'princess': 1
    }
    return render(request, "The_Unicorn_Invasion.html", context)

def princess_two(request):
    context = {
        'unicorn_choice': 1 ,
        'princess': 2
    }
    return render(request, "The_Unicorn_Invasion.html", context)

def princess_three(request):
    context = {
        "princess": 3
    }
    return render(request, "The_Unicorn_Invasion.html", context)

def death_one(request):
    context = {
        "death": 1
    }
    return render(request, "death.html", context)

def kitchen_one(request):
    context = {
        "kitchen": 1 ,
        "Roll": 0
    }
    return render(request, "The_Unicorn_Invasion.html", context)


def stealth(request):
    stealth = random.randint(1, 20)
    context={
        'Roll': stealth, 
        "kitchen": 1
    }
    return render(request, 'The_Unicorn_Invasion.html', context)

def bread(request):
    context = {
        'kitchen': "bread"
    }
    return render(request, "The_Unicorn_Invasion.html", context)

def cake(request):
    context = {
        'kitchen': "cake"
    }
    return render(request, "The_Unicorn_Invasion.html", context)

def steak(request):
    context = {
        "kitchen": 'steak'
    }
    return render(request, "The_Unicorn_Invasion.html", context)


def prologue(request):
    return render(request, "prologue.html")

def death_stealing(request):
    context = {
        'death': 2
    }
    return render(request, "death.html", context)