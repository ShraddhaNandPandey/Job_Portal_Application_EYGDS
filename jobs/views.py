from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.models import User

def landing_page(request):
    isAuthenticated = request.user.is_authenticated
    return render(request, 'landing.html', {'isAuthenticated': isAuthenticated, 'user': request.user})

def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        # Handle form submission here
        # Example: Get form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Perform necessary actions (e.g., create user, save to database)
        # Redirect to a success page or login page
        return redirect('login')  # Change 'login' to your actual login URL name
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        # Handle login form submission here
        # Example: Get form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Perform login authentication (e.g., check username and password against database)
        # If login is successful, redirect to a success page
        # If login fails, render the login page with an error message
        return redirect('home')  # Change 'home' to your landing page URL name
    return render(request, 'login.html')

def hr_page(request):
    return render(request, 'hr.html')

def hr_post_job(request):
    if request.method == 'POST':
        # Process the job posting form data here
        # Example: Save the job details to the database
        # Redirect to a success page or back to the HR dashboard
        return redirect('hr_dashboard')  # Adjust the URL name for the HR dashboard
    else:
        # Handle GET request or display the job posting form
        # Example: Render the job posting form template
        return render(request, 'job_post_form.html')

def my_view(request):
    isAuthenticated = request.user.is_authenticated
    return render(request, 'landing.html', {'isAuthenticated': isAuthenticated})
