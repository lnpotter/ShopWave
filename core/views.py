from django.shortcuts import redirect, render

from item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories, "items": items})

def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def terms(request):
    return render(request, "terms.html")

def policy(request):
    return render(request, "policy.html")

def signup(request):
    form = SignupForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect("/login")
    return render(request, "registration/signup.html", {"form": form})