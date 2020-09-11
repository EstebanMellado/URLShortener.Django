from django.shortcuts import render, redirect
from .models import short_url
from .forms import UrlForm
from .shortener import shortener

# Create your views here.


def Create(request):
    form = UrlForm(request.POST)
    a = ""
    if request.method == 'POST':
        if form.is_valid():
            NewUrl = form.save(commit=False)
            a = shortener().issue_token()
            NewUrl.short_url = a
            NewUrl.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'a': a})


def Redirect(request, token):
    url = short_url.objects.filter(short_url=token)[0]
    return redirect(url.long_url)
