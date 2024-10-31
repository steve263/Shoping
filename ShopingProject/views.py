from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm

def index(request):

    return render(request, 'index.html')

def add_product(request):

    return render(request, 'add-products.html')

def view_products(request):

    return render(request, 'view-product.html')
def register(request):
    global form
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created for {form.cleaned_data["username"]}')
            return redirect('login-url')
        else:
            form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})