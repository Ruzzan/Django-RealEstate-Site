from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from contacts.models import Contact
from myApp.models import Home
from django.contrib.auth.decorators import login_required
# Create your views here.

def SignupView(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            try:
                user = User.objects.get(username = request.POST['username'])
                messages.error(request, 'Username already taken.')
                return render(request, 'accounts/signup.html')
            except User.DoesNotExist:
                user = User.objects.create_user(username = request.POST['username'], password=request.POST['password'],email=request.POST['email'])
                user.first_name = request.POST['first_name']
                user.last_name  = request.POST['last_name']
                user.save()
                auth.login(request, user)
                messages.success(request, "You have been registered.You can Login.")
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html',{'error':'Incorrect Passwords.'})
    else:
        return render(request, 'accounts/signup.html')

def LoginView(request):
    if request.method == 'POST':
        user = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                messages.success(request,"Welcome to Chhey {0}".format(request.user.username))
                return redirect('dashboard')
        else:
            messages.error(request, "Invalid login credentials.")
    return render(request, 'accounts/login.html')

def LogoutView(request):
    auth.logout(request)
    messages.error(request,'You have been logged out.')
    return redirect('login')

@login_required
def DashboardView(request):
    user_contact = Contact.objects.order_by('-date').filter(user_id=request.user.id)
    context = {
        'contacts':user_contact,
        
     
    }
    return render(request, 'accounts/dashboard.html',context)


