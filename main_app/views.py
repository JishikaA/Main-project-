from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from main_app.form import LoginForm, DonorRegister, ReceiverRegister, ReceiverRequest


# Create your views here.
def test(request):
    return render(request,'test.html')
def index_dashboard(request):
    return render(request,'admin_base.html')

def DonorR(request,):
    form1  = LoginForm()
    form2 = DonorRegister()

    if request.method =="POST":
        form1 = LoginForm(request.POST)
        form2 = DonorRegister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_Donor = True
            user1.save()

            user2 = form2.save(commit=False)
            user2.user = user1
            user2.save()
            return redirect("login")


    return render(request,'DonorReceiver.html',{"form1":form1, "form2":form2})

def Receive(request):
    form1  = LoginForm()
    form2 = ReceiverRegister()

    if request.method =="POST":
        form1 = LoginForm(request.POST)
        form2 = ReceiverRegister(request.POST)

        if form1.is_valid() and form2.is_valid():
            user1 = form1.save(commit=False)
            user1.is_Receiver = True
            user1.save()

            user2 = form2.save(commit=False)
            user2.user = user1
            user2.save()
            return redirect("login1")


    return render(request,'Receiver.html',{"form1":form1, "form2":form2})

def index(request):
    return render(request,'index.html')

def Login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        print(username)
        password = request.POST.get('pass')
        print(password)
        user =authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request, user)
            if user.is_staff:

                return redirect('admin_base')
            elif user.is_Donor:

                return redirect('donor_base')
            elif user.is_Receiver:

                return redirect('receiver_base')
        else:
            messages.info(request,'invalid Credentials')
    return render(request,'Login.html')
