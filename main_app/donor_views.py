from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.filters import BloodFilter
from main_app.form import DonorRegister
from main_app.models import Receiver_Request, Donor, Receiver

@login_required(login_url='login')
def donor(request):
    return render(request,'donor/donor_base.html')

# def blood(request):
#     data =Receiver_Request.objects.all()
#     bgFilter =BloodFilter(request.GET, queryset=data)
#     data =bgFilter.qs
#     return render(request,'donor/donor_request.html',{'data':data,'bgFilter':bgFilter})
@login_required(login_url='login')
def donor_request(request):
    data =Receiver_Request.objects.all()
    bgFilter = BloodFilter(request.GET, queryset=data)
    data = bgFilter.qs
    return render(request, 'donor/donor_request.html', {'data': data, 'bgFilter': bgFilter})

@login_required(login_url='login')
def donate(request,id):
    obj =Receiver_Request.objects.get(id=id)
    user1=request.user
    data=Donor.objects.get(user=user1)
    obj.Donor_name=data
    obj.Status =1
    obj.save()
    return redirect('donorre')

@login_required(login_url='login')
def donation(request):
    return render(request,'admin/donation_accept.html')

@login_required(login_url='login')
def profile(request):
    user1 =request.user
    data =Donor.objects.get(user=user1)
    return render(request,'donor/profile.html',{'form':data})

@login_required(login_url='login')
def donor_update(request,id):
    data = Donor.objects.get(id=id)
    form = DonorRegister(instance=data)

    if request.method == "POST":
        todo = DonorRegister(request.POST, request.FILES, instance=data)
        if todo.is_valid():
            todo.save()
            return redirect("profile")
    return render(request, 'donor/profile_update.html', {'form': form})

def logou(request):
    logout(request)
    return redirect("/")