from django.shortcuts import redirect, render
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Menu, MenuItem
from .forms import *

@login_required
def create_menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id, owner=request.user)

    if request.method == 'POST':
        menu_form = MenuForm(request.POST)
        item_formset = MenuItemFormSet(request.POST, prefix='items')

        if menu_form.is_valid() and item_formset.is_valid():
            menu = menu_form.save(commit=False)
            menu.restaurant = restaurant
            menu.save()

            for form in item_formset:
                if form.cleaned_data:
                    item = form.save(commit=False)
                    item.menu = menu
                    item.save()

            return redirect('restaurant-detail', restaurant_id=restaurant_id)
    else:
        menu_form = MenuForm()
        item_formset = MenuItemFormSet(prefix='items')

    context = {
        'restaurant': restaurant,
        'menu_form': menu_form,
        'item_formset': item_formset,
    }

    return render(request, 'create_menu.html', context)
