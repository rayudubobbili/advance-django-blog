from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Subscribers
from .forms import Subscriber_form


def subscriber(request):
    if request.method == 'POST':
        form = Subscriber_form(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'subscriber/success.html')
    else:
        form = Subscriber_form()
    return render(request, 'subscriber/new-subscriber.html', {'form': form})


def subscriber_cancel_form(request):
    if request.method == 'POST':
        form = Subscriber_form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subscriber = get_object_or_404(Subscribers, name=name)
            if subscriber.email == email:
                Subscribers.objects.get(name=name).delete()
                return render(request, 'subscriber/subscriber-cancel-success.html')
            else:
                return render(request, 'subscriber/wrong.html')
        else:
            return render(request, 'subscriber/wrong.html')
    else:
        form = Subscriber_form()
    return render(request, 'subscriber/subscriber-cancel.html', {'form': form})


def subscriber_cancel(request, name):
    subscriber = get_object_or_404(Subscribers, name=name)
    subscriber.delete()
    return render(request, 'subscriber/subscriber-cancel-success.html')
    if not subscriber:
        return Http404("Something went wrong. Check the user name correctly")
