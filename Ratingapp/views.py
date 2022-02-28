from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import auth, User
from .models import Category, Product, Ratings

def save(request):
    if request.method == 'POST':
        first_name   = request.POST['name']
        username = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['confirm']
        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'EMAIL already taken!!!!!')
                return render(request, 'login.html')
            else:
                user = User.objects.create_user(first_name=first_name, email=email, password=password,
                                                username=username)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, 'PASSWORD not matching!!!')
            return render(request, 'login.html')
    else:
        pass
    
def login(request):
    return render(request, 'login.html')

def store(request):
    if request.method == 'POST':
        first_name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=first_name, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            messages.info(request, 'Name or Password not matching')
            return render(request, 'login.html')
    else:
        pass
    
def logout(request):
    auth.logout(request)
    return render(request, 'home.html')

def home(request):
    category = Category.objects.all()
    return render(request, 'home.html', {'category': category})

def details(request, id):
    product = Product.objects.filter(Category=id)
    return render(request, 'details.html', {'product1': product})

def description(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'description.html', {'product2': product})

def review(request, id, user_id, Category_id):
    user = User.objects.all()
    category = Category.objects.get(id=Category_id)
    y = Ratings(review=request.POST['review'], rating=request.POST['rating'], product=Product.objects.get(id=id),
               user=User.objects.get(id=user_id))
    y.save()
    return render(request, 'home.html', {'user': user}, {'category': category})
    