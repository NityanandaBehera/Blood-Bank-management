from django.shortcuts import redirect, render
from .models import Donor, Camp
from .forms import DonorForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.core.paginator import Paginator


def Home(request):
    return render(request, 'base.html')


def register(request):
    page = 'register'
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, ("Account created successfully"))
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, ("Error creating your account"))
    context = {
        'page': page, 'form': form
    }
    return render(request, 'login.html', context)


def Login(request):
    page = 'register'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, ("username doesn't exist"))
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, ("username or password is incorrect"))
    return render(request, 'login.html')


def Logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def DonorView(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, ('Your Blood_group was successfully added!'))
        else:
            messages.error(request, ('Error in adding Blood_group!'))
        return redirect('home')
    else:
        donor = Donor.objects.all()
        form = DonorForm()
        context = {'donor': donor, 'form': form}
        return render(request, 'donor.html', context)


@login_required(login_url='login')
def Camping(request):
    camp = Camp.objects.all()
    context = {'camp': camp}
    return render(request, 'camping.html', context)


def Details(request, pk):
    donor = Donor.objects.get(id=pk)
    context = {'donor': donor}
    return render(request, 'details.html', context)


@login_required(login_url='login')
def DonorList(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    donor = Donor.objects.filter(
        Q(blood_group__icontains=search_query) | Q(adress__icontains=search_query))

    context = {'donor': donor, 'search_query': search_query, }
    return render(request, 'donor-list.html', context)
