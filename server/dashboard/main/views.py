from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from .models import CustomerModel
from .forms import CustomerForm
from django.views import View


def home(request):
    return render(request,'main/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','password1':'','password2':''}
        form = UserCreationForm(initial= initial_data)

    return render(request,'auth/register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username':'','password' :''}
        form = AuthenticationForm(initial= initial_data)

    return render(request,'auth/login.html',{'form':form})


def dashboard_view(request):
    customers = CustomerModel.objects.all()
    return render(request, 'main/dashboard.html', {'customers':customers})


def logout_view(request):
    logout(request)
    return redirect('login')

class CustomerView(View):
    def get(self, request):
        form = CustomerForm()
        return render(request, 'main/add_customer.html', {'form': form})

    def post(self, request):
        form = CustomerForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('dashboard')  
        return render(request, 'main/add_customer.html', {'form': form})