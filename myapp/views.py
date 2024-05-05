from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash 	
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .models import employee, Property
from django.core.files.storage import FileSystemStorage
from django.conf import settings

# Views for the application

def index(request):
    data = Property.objects.all()
    return render(request, "index.html", {'data': data})

def login(request):
    return render(request, "login.html")

def registration(request):
    return render(request, "registration.html")

def register(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')

        hashed_password = make_password(password)

        user = employee.objects.create(fname=fname,lname=lname,email=email,password=hashed_password,usertype=usertype)
        #Employee.objects.create(user=user, usertype=usertype)

        messages.success(request, "Registration successfully completed")
        return redirect("login")
    else:
        return redirect("registration")

def login_check(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        usertype = request.POST.get('usertype')

        try:
            user = employee.objects.get(email=email, usertype=usertype)  # Assuming usertype is a valid field
            if check_password(password, user.password):
                # Password matches, proceed with login
                request.session['username'] = user.email
                request.session['name'] = user.fname
                request.session['usertype'] = usertype
                return redirect('index')
            else:
                # Password does not match
                messages.error(request, "Invalid login details")
                return redirect('login')
        except employee.DoesNotExist:
            # No user found
            messages.error(request, "Invalid login details")
            return redirect('login')
def logout(request):
    del request.session["username"]
    del request.session["name"]
    a = request.session.get('usertype')
    if a:
       del request.session["usertype"]
    return render(request,"login.html")

@login_required
def propertys(request):
    data = Property.objects.all()
    return render(request, "propertys.html", {'data': data})

@login_required
def search_property(request):
    data = Property.objects.all()
    return render(request, "search_property.html", {'data': data})

@login_required
def dashboard(request):
    data = Property.objects.filter(email=request.user.email)
    return render(request, "dashboard.html", {'data': data})

def demo(request):
    return redirect('demo')

@login_required
def Upload_property(request):
    if request.method == "POST":
        images = request.FILES.getlist('propertyImages')  # Handle multiple image files
        description = request.POST.get('propertyDescription')
        area = request.POST.get('propertyArea')
        beds = request.POST.get('propertyBeds')
        baths = request.POST.get('propertyBaths')
        garages = request.POST.get('propertyGarages')
        price = request.POST.get('propertyPrice')
        location = request.POST.get('propertyLocation')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pin = request.POST.get('pin')
        contact = request.POST.get('contactDetails')
        email = request.user.email  # Use the email of the logged-in user

        property_instance = Property(propertyDescription=description, propertyArea=area, propertyBeds=beds, propertyBaths=baths, propertyGarages=garages, propertyPrice=price, propertyLocation=location, city=city, state=state, pin=pin, contactDetails=contact, email=email)
        property_instance.save()

        # Saving images to the FileSystem
        fs = FileSystemStorage()
        for image in images:
            filename = fs.save(image.name, image)
            property_instance.images.add(filename)  # Assuming Property model has an 'images' field to store uploaded files

        return redirect('dashboard')
    return render(request, "upload_property.html")

@login_required
def Your_property(request):
    return render(request, "your_property.html")

@login_required
def property_details(request):
    property_id = request.GET.get('id')
    data = Property.objects.filter(id=property_id)
    return render(request, "property_details.html", {'data': data})

@login_required
def search(request):
    city = request.GET.get('city')
    data = Property.objects.filter(city=city)
    return render(request, "search_property.html", {'data': data})
