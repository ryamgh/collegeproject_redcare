

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from .models import  *
from django.contrib import messages
from .forms import SignUpForm
from .forms import CustomUserForm
from .forms import RequestBloodForm



def home(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        #Authenticate user
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"Login Sucessful...")
            return redirect('home')
        else:
            messages.success(request,"Invalid! Please try again. ")
            return redirect('home')
    else:
        return render(request,'home.html',{})
def logout_user(request): 
    logout(request)  
    messages.success(request,"You Have Been Logged Out") 
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Save CustomUser data
            custom_user = form.save(commit=False)
            custom_user.save()

            # Save additional data to related models
            blood_type = form.cleaned_data['blood_group']
            user_full_name = form.cleaned_data['full_name']

            # Create or update Blood model instance
            blood_obj, created = Blood.objects.get_or_create(type=blood_type)

            # Update CustomUser with full_name and blood_group
            custom_user.full_name = user_full_name
            custom_user.blood_group = blood_type
            custom_user.save()

            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
 

def request_blood(request):
    return render(request,'requestblood.html',{})
def profile(request):
    return render(request,'profile.html',{})
    
def sucess_page(request):
    return render(request,'success.html',{})


def edit_profile(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to profile page after successful update
    else:
        form = CustomUserForm(instance=user)
    return render(request, 'editprofile.html', {'form': form})





def request_blood_list(request):
    if request.method == 'POST':
        form = RequestBloodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        blood_requests = RequestBlood.objects.all()
        form = RequestBloodForm()
    return render(request, 'seeallrequest.html', {'blood_requests': blood_requests, 'form': form})


def request_blood(request):
    if request.method == 'POST':
        form = RequestBloodForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data['phone']
            city = form.cleaned_data['city']
            address = form.cleaned_data['address']
            blood_group = form.cleaned_data['blood_group']
            date = form.cleaned_data['date']
            Request = RequestBlood(phone=phone, city=city, address=address, blood_group=blood_group, date=date)
            Request.save()
            return redirect('success')  # Redirect to success page after successful update
    else:
        form = RequestBloodForm()
    return render(request, 'requestblood.html', {'form': form})





    
