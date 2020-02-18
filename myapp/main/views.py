from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Sum

from datetime import datetime, timezone, timedelta
from main.forms import UpdateForm # ModelForm
from main.models import Update # Model
import pytz


def home(request):
    # gets data to display on homepage
    starbucks_display, dunkin_display, SB_elapsed, DD_elapsed = getUpdates(request)
    
    args = ({'starbucks_display': starbucks_display, 
            'dunkin_display': dunkin_display,
            'SB_elapsed': SB_elapsed,
            'DD_elapsed': DD_elapsed
            })
    return render(request, 'main/home.html', args)


@login_required
def update_options(request):
    # user can only update once every 10 minutes : 10 set in model
    # try/catch checks if user is in updates table -> in not they are updating for the first time so catch
    try:
        user_latest_update = Update.objects.filter(user=request.user).latest('id')
    except:
        user_latest_update = None

    if user_latest_update != None:
        current_time = datetime.now().replace(tzinfo=None)   
        next_allowed_update = user_latest_update.next_allowed_update.replace(tzinfo=None)
        if current_time > next_allowed_update:
            return render(request, 'main/update-options.html')
        else:
            return render(request, 'main/update-time-denied.html')
    else:
        return render(request, 'main/update-options.html')


@login_required
def starbucks(request):
    # Prevents direct access to update page from browser
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url is None:
        return redirect('main-home')
    form = UpdateForm(request.POST or None)
    starbucks_display, dunkin_display, SB_elapsed, DD_elapsed = getUpdates(request)   
    if request.method == "POST":
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.location = 'starbucks'
            update.date = datetime.now()
            update.next_allowed_update=datetime.now()+timedelta(minutes=1)-timedelta(hours=5)
            update.save()
            value = form.cleaned_data['update']
            return redirect('main-home')
    args = {'form': form, 
            'line': starbucks_display}
    return render(request, "main/starbucks.html", args)


@login_required
def dunkin(request):
    # Prevents direct access to update page from browser
    previous_url = request.META.get('HTTP_REFERER')
    if previous_url is None:
        return redirect('main-home')
    form = UpdateForm(request.POST or None)
    starbucks_display, dunkin_display, SB_elapsed, DD_elapsed = getUpdates(request)   
    if request.method == "POST":
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.location = 'dunkindonuts'
            update.date = datetime.now()
            update.next_allowed_update=datetime.now()+timedelta(minutes=1)-timedelta(hours=5)
            update.save()
            value = form.cleaned_data['update']
            return redirect('main-home')
    args = {'form': form, 
            'line': dunkin_display}
    return render(request, "main/dunkin.html", args)


def location_denied(request):
    return render(request, 'main/user-location-denied.html')


def location_unavailable(request):
    return render(request, 'main/user-location-unavailable.html')


def location_invalid(request):
    return render(request, 'main/user-location-invalid.html')


def offline(request):
    return render(request, 'main/offline.html')


@login_required
def request_options(request):
    return render(request, 'main/request-options.html')


def request_sent(request):
    return render(request, 'main/request-sent.html')


def offline(request):
    return render(request, 'main/offline.html')

def getUpdates(request):
    # this is used to get the elapsed time of the most recent update
    starbucks_latest_line_update = Update.objects.filter(location='starbucks').latest('id')    
    dunkindonuts_latest_line_update = Update.objects.filter(location='dunkindonuts').latest('id')
    SB_elapsed = getElapsed(request, starbucks_latest_line_update)
    DD_elapsed = getElapsed(request, dunkindonuts_latest_line_update)
    
    #gets the average line length for each location for the last 2 min
    current_time = datetime.now().replace(tzinfo=None)
    time_threshold = current_time - timedelta(minutes=2)
    starbucks_avg = Update.objects.filter(date__gte = time_threshold, location='starbucks').aggregate(Avg('update'))
    dunkindonuts_avg = Update.objects.filter(date__gte = time_threshold, location='dunkindonuts').aggregate(Avg('update'))

    # get starbucks value | avg is none display latest > else average last 2 min
    if starbucks_avg.get('update__avg') == None:
        starbucks_display = starbucks_latest_line_update.update
    else:
        starbucks_display = starbucks_avg.get('update__avg')

    # get dunkin value | avg is none display latest > else average last 2 min
    if dunkindonuts_avg.get('update__avg') == None:
        dunkin_display = dunkindonuts_latest_line_update.update
    else:
        dunkin_display = dunkindonuts_avg.get('update__avg')

    starbucks_display = round(starbucks_display)
    dunkin_display = round(dunkin_display)
    return starbucks_display, dunkin_display, SB_elapsed, DD_elapsed


# calculates elapsed time from the most recent update for home GUI
def getElapsed(request, store):
    current_time = datetime.now(timezone.utc)
    elapsed_time_formatted = current_time - store.date
    elapsed_array = str(elapsed_time_formatted).split(':')
    
    # [hh][mm][ss]
    # [0][mm][ss]
    # [0][0][ss]
    
    if elapsed_array[0] == '0' and elapsed_array[1] == '00':
        #  seconds --> [0][0][ss]
        return " just seconds ago "
    elif elapsed_array[0] == '0' and elapsed_array[1] != '00':
        # minutes -->[0][mm][ss]
        elapsed = str(elapsed_array[1]).lstrip("0")
        if elapsed == '1':
            return " 1 minute ago"
        else:
            return " "+elapsed+" minutes ago "
    else:
        # hours --> [hh][mm][ss]
        if elapsed_array[0] == '1':
            return " 1 hour ago "
        else:
            elapsed = str(elapsed_array[0]).lstrip("0")
            return " "+elapsed_array[0]+" hours ago"