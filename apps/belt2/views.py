from django.shortcuts import render, redirect, HttpResponse
from .models import User, Poke
from django.contrib import messages
from django.db.models import Count, Sum
# Create your views here.
def index(request):
    return render(request, 'belt2/index.html')

def pokeboard(request):
    if 'userid' in request.session:
        allusers = User.objects.all().annotate(poke_count=Count('poked'))
        mypokes = User.objects.filter(id=request.session['userid']).annotate(poke_count=Count('poked_by'))
        allpokers = Poke.objects.filter(pokee=request.session['userid']).annotate(poke_count=Count('poker'))[:3]
        print allpokers
        context = {
            "currentuser": User.objects.get(id=request.session['userid']),
            'users': allusers,
            'mypokes': mypokes,
            'pokers': allpokers
        }
        return render(request, 'belt2/pokeboard.html', context)
    else:
        return redirect('/')

def poke(request, id):
    result= Poke.objects.newPoke(id, request.session['userid'])
    if result[0]==False:
        messages.error(request, result[1])
    if result[0]==True:
        messages.success(request, result[1])
    return redirect ("/pokeboard")

def register(request):
    if request.method == 'GET':
        return redirect ('/')
    newuser = User.objects.validate(request.POST)
    print newuser
    if newuser[0] == False:
        for each in newuser[1]:
            messages.error(request, each)
        return redirect('/')
    if newuser[0] == True:
        messages.success(request, 'Well done')
        request.session['userid'] = newuser[1].id
        return redirect('/pokeboard')

def login(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        user = User.objects.login(request.POST)
        print user
        if user[0] == False:
            for each in user[1]:
                messages.add_message(request, messages.INFO, each)
            return redirect('/')
        if user[0] == True:
            messages.add_message(request, messages.INFO,'Welcome, You are logged in!')
            request.session['userid'] = user[1].id
            return redirect('/pokeboard')

def logout(request):
    if 'userid' not in request.session:
        return redirect('/')
    print "*******"
    print request.session['userid']
    del request.session['userid']
    return redirect('/')
