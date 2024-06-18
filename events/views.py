from django.shortcuts import render, get_object_or_404, redirect
from .models import SportEvent, MemberClient
from .forms import SportEventForm, MemberClientForm

# Event views
def event_list(request):
    events = SportEvent.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_detail(request, pk):
    event = get_object_or_404(SportEvent, pk=pk)
    return render(request, 'events/event_detail.html', {'event': event})

def event_new(request):
    if request.method == "POST":
        form = SportEventForm(request.POST)
        if form.is_valid():
            event = form.save()
            return redirect('event_list')
    else:
        form = SportEventForm()
    return render(request, 'events/event_edit.html', {'form': form})

def event_edit(request, pk):
    event = get_object_or_404(SportEvent, pk=pk)
    if request.method == "POST":
        form = SportEventForm(request.POST, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('event_detail', pk=event.pk)
    else:
        form = SportEventForm(instance=event)
    return render(request, 'events/event_edit.html', {'form': form})

def event_delete_select(request):
    events = SportEvent.objects.all()
    return render(request, 'events/event_delete_select.html', {'events': events})

def event_delete_confirm(request, pk):
    event = get_object_or_404(SportEvent, pk=pk)
    if request.method == "POST":
        event.delete()
        return redirect('event_list')
    return render(request, 'events/event_delete_confirm.html', {'event': event})

# Client views

def client_list(request):
    clients = MemberClient.objects.all()
    return render(request, 'index.html', {'clients': clients})
def client_list(request):
    clients = MemberClient.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(MemberClient, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})

def client_new(request):
    if request.method == "POST":
        form = MemberClientForm(request.POST)
        if form.is_valid():
            client = form.save()
            return redirect('client_list')
    else:
        form = MemberClientForm()
    return render(request, 'clients/client_edit.html', {'form': form})

def client_edit(request, pk):
    client = get_object_or_404(MemberClient, pk=pk)
    if request.method == "POST":
        form = MemberClientForm(request.POST, instance=client)
        if form.is_valid():
            client = form.save()
            return redirect('client_detail', pk=client.pk)
    else:
        form = MemberClientForm(instance=client)
    return render(request, 'clients/client_edit.html', {'form': form})

def client_delete_select(request):
    clients = MemberClient.objects.all()
    return render(request, 'clients/client_delete_select.html', {'clients': clients})

def client_delete_confirm(request, pk):
    client = get_object_or_404(MemberClient, pk=pk)
    if request.method == "POST":
        client.delete()
        return redirect('client_list')
    return render(request, 'clients/client_delete_confirm.html', {'client': client})
