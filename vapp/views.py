from django.shortcuts import render,redirect
from vapp.models import appointmntdb,contactdb,registerdb,servicebookdb
from adminapp.models import hospitaldb,doctordb,gallerydb,servicedb,deptdb,savedelappointmentdb,savedeldb
from django.contrib import messages

# Create your views here.
def mainpage(req):
    data=hospitaldb.objects.all()
    pro = doctordb.objects.all()
    bro=registerdb.objects.all()
    return render(req,"mainpage.html",{'data':data,'pro':pro,'bro':bro})
def appointmentpage(req):
    data=hospitaldb.objects.all()
    pro=doctordb.objects.all()
    return render(req,"appointmentpage.html",{'data':data,'pro':pro})
def saveappointment(req):
    if req.method=="POST":
        hosp=req.POST.get('hos')
        dept=req.POST.get('dept')
        dctr=req.POST.get('dctr')
        date=req.POST.get('date')
        tym=req.POST.get('time')
        name=req.POST.get('name')
        phn=req.POST.get('phone')
        mail=req.POST.get('email')
        message=req.POST.get('message')
        obj=appointmntdb(hospitalname=hosp,Department=dept,Doctors=dctr,Date=date,time=tym,Name=name,phonenum=phn,email=mail,Message=message)
        obj.save()
        messages.success(req,"Your Slot Has been Successfully Booked")
        return redirect(appointmentpage)
def about(req):
    data=doctordb.objects.all()
    prodata=gallerydb.objects.all()
    return render(req,"about.html",{'data':data,'prodata':prodata})
def service(req):
    bros=doctordb.objects.all()
    data=servicedb.objects.all()
    return render(req,"service.html",{'data':data,'bros':bros})
def department(req):
    pros=doctordb.objects.all()
    data=deptdb.objects.all()
    return render(req,"department.html",{'data':data,'pros':pros})
def singledepartment(req,depname):
    pros=doctordb.objects.all()
    data=deptdb.objects.filter(deptname=depname)
    return render(req,"singledepartment.html",{'data':data,'pros':pros})
def doctor(req):
    data=doctordb.objects.all()
    return render(req,"doctor.html",{'data':data})
def singledoctor(req,pro):
    pata=doctordb.objects.all()
    data=doctordb.objects.filter(doctorname=pro)
    return render(req,"singledoctor.html",{'data':data,'pata':pata})
def contact(req):
    data=doctordb.objects.all()
    return render(req,"contact.html",{'data':data})
def savecontact(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        query=req.POST.get('subject')
        phn=req.POST.get('phone')
        mess=req.POST.get('message')
        obj=contactdb(name=na,emailadd=em,query=query,phnnum=phn,message=mess)
        obj.save()
        messages.success(req,"Your Contact Has been successfully submitted")
        return redirect(contact)
# def medicines(req):
#     data=medicinedb.objects.all()
#     return render(req,"medicines.html",{'data':data})
# def singlemedicine(req,medi):
#     medic=medicinedb.objects.filter(medicinename=medi)
#     return render(req,"singlemedicine.html",{'medic':medic})
# def cartmedicine(req):
#     return render(req,"cartmedicine.html")
# def savecart(req):
#     if req.method=="POST":
#         mnae=req.POST.get('medicinename')
#         pr=req.POST.get('price')
#         dis=req.POST.get('dis')
#         qty=req.POST.get('qty')
#         tpr=req.POST.get('totalprice')
#         obj=cartdb(Medicinename=mnae,price=pr,description=dis,qty=qty,totalprice=tpr)
#         obj.save()
#         return redirect(cartmedicine)
def register(req):
    return render(req,"userregistration.html")
def saveregister(req):
    if req.method=="POST":
        fn=req.POST.get('fname')
        ln=req.POST.get('lname')
        dob=req.POST.get('date')
        gender=req.POST.get('g')
        email=req.POST.get('email')
        ph=req.POST.get('phone')
        password=req.POST.get('password')
        rpassword=req.POST.get('rpassword')
        obj=registerdb(firstname=fn,lastname=ln,dateofbirth=dob,gender=gender,email=email,number=ph,password=password,repeatpassword=rpassword)
        obj.save()
        messages.success(req,"User Created Successfully")
        return redirect(login)
def login(req):
    return render(req,"login.html")
def userlogin(req):
    if req.method=="POST":
        uname=req.POST.get('email')
        pswd=req.POST.get('password')
        if registerdb.objects.filter(email=uname,password=pswd).exists():
            req.session['email']=uname
            req.session['password']=pswd
            messages.success(req,"You have successfully login")
            return redirect(mainpage)
        else:
            messages.error(req,"Incorrect Password or Username")
            return redirect(login)
    else:
        messages.error(req,"Incorrect Password or Username")
        return redirect(login)
def logout(req):
    del req.session['email']
    del req.session['password']
    messages.success(req,"Successfully Logged Out")
    return redirect(login)
def bookservice(req):
    data=servicedb.objects.all()
    pata=doctordb.objects.all()
    return render(req,"bookservice.html",{'data':data,'pata':pata})
def savebooking(req):
    if req.method=="POST":
        sr=req.POST.get('serv')
        da=req.POST.get('date')
        ty=req.POST.get('time')
        na=req.POST.get('name')
        ph=req.POST.get('phone')
        em=req.POST.get('email')
        mes=req.POST.get('message')
        obj=servicebookdb(servicename=sr,date=da,time=ty,fullname=na,phone=ph,email=em,message=mes)
        obj.save()
        messages.success(req,"Your Slot has been Successfully Booked")
        return redirect(bookservice)
def profile(req,pr):
    data=registerdb.objects.filter(email=req.session['email'])

    return render(req,"profile.html",{'data':data})
def editprofile(req,dataid):
    data=registerdb.objects.get(id=dataid)
    return render(req,"editprofile.html",{'data':data})
def updateprofile(req,dataid):
    if req.method=="POST":
        fn = req.POST.get('fname')
        ln = req.POST.get('lname')
        dob = req.POST.get('date')
        gender = req.POST.get('g')
        email = req.POST.get('email')
        ph = req.POST.get('phone')
        f=registerdb.objects.get(id=dataid)
        registerdb.objects.filter(id=dataid).update(firstname=fn,lastname=ln,dateofbirth=dob,gender=gender,email=email,number=ph)
        messages.success(req,"data updated")

        return redirect(mainpage)
def history(req):
    cata=savedelappointmentdb.objects.filter(email=req.session['email'])
    data=registerdb.objects.filter(email=req.session['email'])
    return render(req,"history.html",{'data':data,'cata':cata})