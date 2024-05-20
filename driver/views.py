# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Ambulance, HireRequest, Message, Driver
from .forms import HireRequestForm, MessageForm, DriverForm, AmbulanceForm



@login_required
def add_ambulance(request):
    if request.method == 'POST':
        form = AmbulanceForm(request.POST)
        if form.is_valid():
            ambulance = form.save(commit=False)
            driver = Driver.objects.get(user=request.user)
            ambulance.driver = driver
            ambulance.save()
            messages.success(request, 'Ambulance added successfully!')
            return redirect('driver_profile')
    else:
        form = AmbulanceForm()
    return render(request, 'add_ambulance.html', {'form': form})


def available_ambulances(request):
    ambulances = Ambulance.objects.filter(status='available')
    return render(request, 'available_ambulances.html', {'ambulances': ambulances})

@login_required
def send_message(request, ambulance_id):
    ambulance  = get_object_or_404(Ambulance, id = ambulance_id)
    driver = ambulance.driver  # Assuming each ambulance has one driver

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.receiver = driver.user  # Assuming the driver is linked to a user
            message.save()
            messages.success(request, 'Message sent successfully!')
            return redirect('ambulance_detail', ambulance_id=ambulance.id)
    else:
        form = MessageForm()

    return render(request, 'send_message.html', {'form': form, 'ambulance': ambulance})


@login_required
def hire_request(request, ambulance_id):
    ambulance = get_object_or_404(Ambulance, id=ambulance_id)
    if request.method == 'POST':
        form = HireRequestForm(request.POST)
        if form.is_valid():
            hire_request = form.save(commit=False)
            hire_request.user = request.user
            hire_request.ambulance = ambulance
            hire_request.save()
            return redirect('available_ambulances')
    else:
        form = HireRequestForm()
    return render(request, 'hire_request.html', {'form': form, 'ambulance': ambulance})

@login_required
def ambulance_detail(request, ambulance_id):
    ambulance = get_object_or_404(Ambulance, id=ambulance_id)
    
    hire_request_form = HireRequestForm()
    message_form = MessageForm()

    if request.method == 'POST':
        if 'send_message' in request.POST:
            message_form = MessageForm(request.POST)
            if message_form.is_valid():
                message = message_form.save(commit=False)
                message.sender = request.user
                if ambulance.driver:
                    message.receiver = ambulance.driver.user  # assuming each ambulance has one driver
                    message.save()
                    messages.success(request, 'Message sent successfully!')
                else:
                    messages.error(request, 'This ambulance has no driver assigned.')
                return redirect('ambulance_detail', ambulance_id=ambulance_id)

    return render(request, 'ambulance_detail.html', {
        'ambulance': ambulance,
        'hire_request_form': hire_request_form,
        'message_form': message_form,
    })
    
    
    
@login_required
def driver_hire_requests(request):
    driver = Driver.objects.get(user=request.user)
    hire_requests = HireRequest.objects.filter(ambulance__in=driver.ambulances.all())
    return render(request, 'driver_hire_requests.html', {'hire_requests': hire_requests})



@login_required
def driver_messages(request):
    try:
        driver = request.user.driver
        messages = Message.objects.filter(receiver=request.user)
    except Driver.DoesNotExist:
        messages = []
    return render(request, 'driver_messages.html', {'messages': messages})

@login_required
def update_hire_request(request, request_id):
    hire_request = get_object_or_404(HireRequest, id=request_id)
    
    if request.method == 'POST':
        status = request.POST.get('status')
        if status in ['accepted', 'rejected']:
            hire_request.status = status
            hire_request.save()
            # Add a success message
            if status == 'accepted':
                messages.success(request, f'Hire request from {hire_request.user.username} accepted.')
            else:
                messages.success(request, f'Hire request from {hire_request.user.username} rejected.')
    
    # Redirect back to the driver's hire requests page
    return redirect('driver_hire_requests')

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