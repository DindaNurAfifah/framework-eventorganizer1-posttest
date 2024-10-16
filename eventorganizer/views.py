from django.shortcuts import render, redirect, get_object_or_404
from .models import Events
from django.db.models import Q
from .forms import EventsForm
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.
def homepage(request):
    event = Events.objects.all()
    return render(request, 'homepage/index.html', {'events': event})

def about(request):
    return render(request, 'homepage/about.html')

# READ Events
def read_events(request):
    query = request.GET.get('q')
    events = Events.objects.all()
    
    if query:
        events = Events.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(category__icontains=query) |
            Q(theme__icontains=query) |
            Q(organizer__name__icontains=query) |
            Q(organizer__location__icontains=query) |
            Q(image__icontains=query) 
        )
    
    return render(request, 'events/index.html', {'events': events, 'query': query})

# CREATE Events
def create_events(request):
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            messages.success(request, 'Events successfully created!.')  
            return redirect('read_events')
        else:
            print(form.errors)
            messages.error(request, 'Events failed to created.')
    else:
        form = EventsForm()
    
    return render(request, 'events/create.html', {'form': form})

# UPDATE Events
def update_events(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Events data successfully changed!')
            return redirect('read_events')
        else:
            print(form.errors)
            messages.error(request, 'Events failed to changed.')
    else:
        form = EventsForm(instance=event)
    
    return render(request, 'events/update.html', {'form': form, 'event': event})

# DELETE Events
def delete_events(request, event_id):
    event = get_object_or_404(Events, id=event_id)
    event.delete()
    messages.success(request, 'Events successfully deleted!')
    return JsonResponse({'success': True})