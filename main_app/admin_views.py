from email.feedparser import FeedParser

from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.db.transaction import commit
from django.dispatch import receiver
from django.shortcuts import render, redirect
from pyexpat.errors import messages

from main_app.form import DonorRegister, Fdbk
from main_app.models import Donor, Receiver, Receiver_Request, Feedback

@login_required(login_url='login')
def admin_base(request):
    return render(request,'admin/admin_base.html')
@login_required(login_url='login')
def read(request):
    data =Donor.objects.all
    return render(request,'admin/read.html',{'data':data})

@login_required(login_url='login')
def remove(request,id):
    data =Donor.objects.get(id=id)
    data.delete()
    return redirect("read")

@login_required(login_url='login')
def update(request,id):
    data =Donor.objects.get(id=id)
    form =DonorRegister(instance=data)

    if request.method =="POST":
        todo =Donor(request.POST,instance=data)
        if todo.is_valid():
            todo.save()
            return redirect("read")
        return render(request, 'update.html', {'form': form})

@login_required(login_url='login')
def read1(request):
    data =Receiver.objects.all
    return render(request,'admin/read.html',{'data':data})

@login_required(login_url='login')
def remove1(request,id):
    data =Receiver.objects.get(id=id)
    data.delete1()
    return redirect("read")

@login_required(login_url='login')
def update1(request,id):
    data =Receiver.objects.get(id=id)
    form =Receiver(instance=data)

    if request.method =="POST":
        todo =Receiver(request.POST,instance=data)
        if todo.is_valid():
            todo.save()
            return redirect("read")
        return render(request, 'update.html', {'form': form})

@login_required(login_url='login')
def table_request(request):
    obj =Receiver_Request.objects.all()
    return render(request,'admin/table_request.html',{'data':obj})

@login_required(login_url='login')
def donation_request(request):
    obj =Receiver_Request.objects.filter(Status=1)
    return render(request,'admin/donation_accept.html',{'data':obj})

@login_required(login_url='login')
def accept(request,id):
    obj =Receiver_Request.objects.get(id=id)
    obj.Status = 2
    obj.save()
    return redirect('dndr')

@login_required(login_url='login')
def reject(request,id):
    obj =Receiver_Request.objects.get(id=id)
    obj.Status = 0
    obj.save()
    return redirect('dndr')

@login_required(login_url='login')
def accept_view(request):
    obj =Receiver_Request.objects.filter(Status=2)
    return render(request,'admin/accept_view.html',{'data':obj})

@login_required(login_url='login')
def adfdv(request):
    obj = Feedback.objects.all()
    return render(request, 'admin/viewfbdk.html', {"data": obj})

@login_required(login_url='login')
def replay_feedback(request, id):
    feedback =Feedback.objects.get(id=id)
    if request.method == "POST":
        r = request.POST.get('Replay')
        feedback.Replay = r
        feedback.save()
        # messages.info(request, 'Replay send for feedback')
        return redirect('adfdv')
    return render(request,"admin/admin_replay.html",{'feedback': feedback})

def logou(request):
    logout(request)
    return redirect("/")


