from django.shortcuts import render ,HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.exceptions import ValidationError
import re
from django.contrib.auth.models import User 


def home(request):
    return render(request,'home.html')
        # return redirect(reverse('quizes'))
    # api_url = "https://api.example.com/data"  # Replace with your actual API URL
    # response = request.get(api_url)
    
    # if response.status_code == 200:
    #     data = response.json()  # Parse the JSON response
    # else:
    #     data = []  # If API request fails, pass an empty list

    # return render(request, 'myapp/api_cards.html', {'data': data})

# Create your views here.

def about(request):
    return render(request,'about.html')

def report(request):
    return render(request,'report.html')

# def quize(request):
#     return render(request,'quize.html')



def contact(request):
    return render(request,'contact.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validation checks
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already in use.")
            return redirect('signup')

        try:
            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Optionally log the user in after signup
            login(request, user)

            messages.success(request, "Account created successfully! You are now logged in.")
            return redirect('home')  # Redirect to the home page or any page you want after signup
        except Exception as e:
            # If there is an issue with account creation
            print(f"Error creating user: {e}")
            messages.error(request, "Error creating account. Please try again.")
            return redirect('signup')

    return render(request, 'signup.html')

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        # Capture the 'next' parameter for post-login redirection
        next_url = request.GET.get('next', reverse('home'))  # Default to home if no 'next' parameter

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect(next_url)  # Redirect to the page user was trying to access before login
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'login.html')
