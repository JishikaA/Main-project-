from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from main_app.form import ReceiverRequest, Fdbk, ReceiverRegister
from main_app.models import Receiver_Request, Receiver, Feedback, Donor


@login_required(login_url='login')
def receiver_base(request):
    return render(request,'receiver/receiver_base.html')

@login_required(login_url='login')
def Request(request):
    data =ReceiverRequest()
    user1 =request.user
    rcvr =Receiver.objects.get(user =user1)

    if request.method == "POST":
        req = ReceiverRequest(request.POST)
        print(req)
        if req.is_valid():
            print("ok")
            obj =req.save(commit=False)
            obj.Receiver_name =rcvr
            obj.save()
    return render(request,'receiver/request.html',{'form':data})

@login_required(login_url='login')
def re_request(request):
    user1 =request.user
    data =Receiver.objects.get(user=user1)
    obj =Receiver_Request.objects.filter(Receiver_name=data)
    return render(request,'receiver/re_request.html',{'data':obj})

@login_required(login_url='login')
def delete_request(request,id):
    data=Receiver_Request.objects.get(id=id)
    data.delete()
    return redirect('req')

@login_required(login_url='login')
def feedback(request):
    data =Fdbk()
    user1 =request.user
    rcvr = Receiver.objects.get(user=user1)

    if request.method == "POST":
        rname =Fdbk(request.POST)
        if rname.is_valid():
            obj = rname.save(commit=False)
            obj.Receiver_name=rcvr
            obj.save()

    return render(request,'receiver/feedback.html',{'data':data})

@login_required(login_url='login')
def fdbv(request):
    user1 = request.user
    data = Receiver.objects.get(user=user1)
    obj = Feedback.objects.filter(Receiver_name=data)
    return render(request, 'receiver/feedbp.html', {'data': obj})

@login_required(login_url='login')
def mypro(request):
    user1 =request.user
    data =Receiver.objects.get(user=user1)
    return render(request,'receiver/my_pro.html',{'form':data})

@login_required(login_url='login')
def receiver_update(request,id):
    data = Receiver.objects.get(id=id)
    form = ReceiverRegister(instance=data)

    if request.method == "POST":
        todo = ReceiverRegister(request.POST, request.FILES, instance=data)
        if todo.is_valid():
            todo.save()
            return redirect("mypro")
    return render(request, 'Receiver/Rprofile_update.html', {'form': form})

def logou(request):
    logout(request)
    return redirect("/")

def donor_view(request):
    data =Donor.objects.all
    return render(request,'receiver/donor_view.html',{'data':data})
# def remove1(request,id):
#     data =Receiver.objects.get(id=id)
#     data.delete1()
#     return redirect("read")