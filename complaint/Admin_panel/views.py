from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#from .forms import ComplaintForm
from .models import ComplaintSystem
#from .forms import UserForm
from django.shortcuts import get_object_or_404
# Create your views here.

def home(request):
    return render(request,'home.html')
def register(request):
    if request.method == 'POST':
        name = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
             user = User.objects.create_user(username=name, first_name=first_name, last_name=last_name, email=email,password=password1)
             user.is_staff = True
             user.is_superuser = True
             user.save()
             messages.success(request, 'Your account has been created! You are able to login')

             return redirect('Login')
        else:
            messages.warning(request, 'Password Mismatching...!!!')
            return redirect('Register')
    else:
        form=CreateUserForm()
        return render(request,'register.html',{'form':form})
@login_required
def profile(request):
    return render(request,"profile.html")
'''def register_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and form.cleaned_data['password1'] == form.cleaned_data['password2']:
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = UserForm()
    return render(request, 'registration.html', {'form': form})'''
'''def complaint_form(request):
    if request.method == 'POST':
        form = ComplaintForm(request.POST)
        if form.is_valid():
            form.save()
            # Add logic for successful form submission if needed
    else:
        form = ComplaintForm()
    return render(request, 'complaint_form.html', {'form': form})'''
def complaintsystem(request):
    mydata = None
    if request.method == 'POST':
        dept=request.POST['dept']
        regno=request.POST['regno']
        username=request.POST['username']
        complaint=request.POST['complaint']
        status=request.POST['status']
        ob=ComplaintSystem()
        ob.dept=dept
        ob.regno=regno
        ob.username=username
        ob.complaint=complaint
        ob.status=status
        ob.save()
    mydata=ComplaintSystem.objects.all()
    return render(request,'page1.html',{'datas':mydata})

def page2(request):
    mydata = ComplaintSystem.objects.all()
    if mydata != '':
        return render(request,'page2.html',{'datas':mydata})
    else:
        return render(request,'page2.html')
def All_complaint(request):
    mydata = ComplaintSystem.objects.all()
    if mydata != '':
        return render(request, 'All_complaint.html', {'datas': mydata})
    else:
        return render(request, 'All_complaint.html')
def update(request,id):
    mydata=ComplaintSystem.objects.get(id=id)
    if request.method=='POST':
        dept = request.POST['dept']
        regno = request.POST['regno']
        complaint = request.POST['complaint']
        status = request.POST['status']
        mydata.dept = dept
        mydata.regno = regno
        mydata.complaint = complaint
        mydata.status = status
        mydata.save()
        return redirect('page2')
    return render(request,'page3.html',{'data':mydata})

'''def com1(request):
    mydata = None  # Initialize 'mydata' outside the if block

    if request.method == 'POST':
        name = request.POST['name']
        regno = request.POST['regno']
        dept = request.POST['dept']
        complaintfor = request.POST['complaintfor']
        obj = Complaint()
        obj.name = name
        obj.regno = regno
        obj.dept = dept
        obj.complaintfor = complaintfor
        obj.save()

    # Retrieve data outside the if block
    mydata = Complaint.objects.all()

    return render(request, 'complaint.html', {'datas': mydata})'''

'''def data(request):
    mydata = Complaint.objects.all()
    return render(request,'displaycomplaint.html',{'datas':mydata})'''