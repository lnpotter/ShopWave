from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView

from .forms import EditItemForm, NewItemForm
from .models import Item

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[:3]
    return render(request, "item/detail.html", {"item": item, "related_items": related_items})

@login_required
def new_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = NewItemForm()
    return render(request, "item/form.html", {"form": form, "title": "New item"})

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect("dashboard:index")

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect("item:detail", pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request, "item/form.html", {"form": form, "title": "Edit item"})

class ItemSearchView(ListView):
    model = Item
    template_name = 'item_search_results.html'
    context_object_name = 'item_list'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Item.objects.filter(name__icontains=query)
        return Item.objects.none()