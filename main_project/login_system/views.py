from django.shortcuts import render, redirect
from  login_system.models import User
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from .models import User
from .forms import RegistrationForm 


#home view
def home(request):
    return render(request, 'home.html')

def test_database_connection(request):
    data_from_db = User.objects.all()
    print("WORKING")
    return render(request, 'test_database.html', {'data_from_db': data_from_db})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.get(Email=email)
            if check_password(password, user.Password):
                # Login successful, set session and redirect
                request.session['user_id'] = user.UserID
                messages.success(request, 'Login successful.')
                return redirect('')  # Replace with your intended redirect URL
            else:
                messages.error(request, 'Invalid email or password.')
        except ObjectDoesNotExist:
            messages.error(request, 'Invalid email or password.')

    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # Replace 'login' with your login page URL
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})