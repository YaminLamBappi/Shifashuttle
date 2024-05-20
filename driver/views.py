# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import DriverForm
from .models import Driver
from django.http import Http404

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .forms import DriverForm
from .models import Driver
from django.urls import reverse

@login_required
def driver_dashboard(request):
    try:
        driver = Driver.objects.get(user=request.user)
        # Redirect to the driver profile if it exists
        return redirect('driver_panel')
    except Driver.DoesNotExist:
        # Redirect to create_driver_profile if the driver profile doesn't exist
        return redirect('create_driver_profile')


@login_required
def edit_driver_profile(request):
    user = request.user
    driver_instance, created = Driver.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES, instance=driver_instance)
        if form.is_valid():
            form.save()
            return redirect('driver_profile')
    else:
        form = DriverForm(instance=driver_instance)

    return render(request, 'edit_driver_profile.html', {'form': form})

@login_required
def create_driver_profile(request):
    user = request.user
    try:
        driver_instance = Driver.objects.get(user=user)
        return redirect('edit_driver_profile')  # If the profile already exists, redirect to edit page
    except Driver.DoesNotExist:
        pass

    if request.method == 'POST':
        form = DriverForm(request.POST, request.FILES)  # Don't pass instance here
        if form.is_valid():
            driver = form.save(commit=False)
            driver.user = request.user
            driver.save()
            messages.success(request, 'Driver profile created successfully!')
            return redirect('driver_profile')
    else:
        form = DriverForm()

    return render(request, 'create_driver_profile.html', {'form': form})


@login_required
def driver_home(request):
    return render(request, "driver_home.html")

@login_required
def driver_panel(request):
    return render(request, "driver_panel.html")

@login_required
def driver_profile(request):
    user = request.user
    try:
        driver = user.driver
    except Driver.DoesNotExist:
        driver = None
    return render(request, 'driver_profile.html', {'driver': driver})