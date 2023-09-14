from django.shortcuts import render,redirect
from adminapp.models import hospitaldb,doctordb,servicedb,medicinedb,gallerydb,deptdb,savedeldb,savedelappointmentdb
from vapp.models import contactdb,appointmntdb,servicebookdb,registerdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import messages



# Create your views here.
def adminpage(req):
    data=appointmntdb.objects.all()
    pata=servicebookdb.objects.all()
    cata=registerdb.objects.all()
    return render(req,"admindashboard.html",{'data':data,'pata':pata,'cata':cata})
def addhospital(req):
    return render(req,"addhospitals.html")
def savehospital(req):
    if req.method=="POST":
        hona=req.POST.get('hos_name')
        hoco=req.POST.get('hos_code')
        hono=req.POST.get('ho_no')
        email=req.POST.get('email')
        address1=req.POST.get('add1')
        address2=req.POST.get('add2')
        states=req.POST.get('state')
        dis=req.POST.get('district')
        pin=req.POST.get('pin')
        obj=hospitaldb(hospitalname=hona,hospitalcode=hoco,contactno=hono,email=email,address1=address1,addrress2=address2,state=states,district=dis,pincode=pin)
        obj.save()
        messages.success(req,"Data has been Successfully Saved")
        return redirect(addhospital)
def displayhospital(req):
    data=hospitaldb.objects.all()
    return render(req,"Displayhospital.html",{'data':data})
def edithospital(req,dataid):
    data=hospitaldb.objects.get(id=dataid)
    return render(req,"edithospital.html",{'data':data})
def updatehospital(req,dataid):
    if req.method=="POST":
        hona = req.POST.get('hos_name')
        hoco = req.POST.get('hos_code')
        hono = req.POST.get('ho_no')
        email = req.POST.get('email')
        address1 = req.POST.get('add1')
        address2 = req.POST.get('add2')
        states = req.POST.get('state')
        dis = req.POST.get('district')
        pin = req.POST.get('pin')
        hospitaldb.objects.filter(id=dataid).update(hospitalname=hona, hospitalcode=hoco, contactno=hono, email=email, address1=address1,
                         addrress2=address2, state=states, district=dis, pincode=pin)
        messages.success(req,"Data has been succesfully Updated")
        return redirect(displayhospital)
def deletehospital(req,dataid):
    data=hospitaldb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"data successfully deleted")
    return redirect(displayhospital)
def adddoctors(req):
    data=hospitaldb.objects.all()
    return render(req,"adddoctors.html",{'data':data})
def savedoctor(req):
    if req.method=="POST":
        hna=req.POST.get('hos_name')
        dna=req.POST.get('doc_name')
        dept=req.POST.get('dept')
        contact=req.POST.get('con_no')
        email=req.POST.get('Email')
        de=req.POST.get('dis')
        photo=req.FILES['image']
        obj=doctordb(hospitalname=hna,doctorname=dna,department=dept,contactnumber=contact,Email=email,Doctor_photo=photo,description=de)
        obj.save()
        messages.success(req,"Data has been succesfully saved")
        return redirect(addhospital)
def displaydoctors(req):
    data=doctordb.objects.all()
    return render(req,"displaydoctors.html",{'data':data})
def editdoctor(req,dataid):
    data=doctordb.objects.get(id=dataid)
    cata=doctordb.objects.all()
    return render(req,"editdoctor.html",{'data':data,'cata':cata})
def updatedoctor(req,dataid):
    if req.method=="POST":
        hna = req.POST.get('hos_name')
        dna = req.POST.get('doc_name')
        dept = req.POST.get('dept')
        contact = req.POST.get('con_no')
        email = req.POST.get('Email')
        de = req.POST.get('dis')
        try:
            img=req.FILES['image']
            im=FileSystemStorage()
            file=im.save(img.name,img)
        except MultiValueDictKeyError:
            file=doctordb.objects.get(id=dataid).Doctor_photo
        doctordb.objects.filter(id=dataid).update(hospitalname=hna,doctorname=dna,department=dept,contactnumber=contact,Email=email,Doctor_photo=file,description=de)
        messages.success(req,"Data Has been Succcessfully Updated")
        return redirect(displaydoctors)

def deletedoctor(req,dataid):
    data=doctordb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"data successfully deleted")
    return redirect(displaydoctors)
def addservices(req):
    return render(req,"addservices.html")
def saveservices(req):
    if req.method=="POST":
        sn=req.POST.get('serv_name')
        pr=req.POST.get('Rates')
        ds=req.POST.get('ds')
        ph=req.FILES['serv_photo']
        obj=servicedb(servicename=sn,rates=pr,description=ds,serv_photo=ph)
        obj.save()
        messages.success(req,"Data has been successfully saved")
        return redirect(addservices)
def displayservices(req):
    data=servicedb.objects.all()
    return render(req,"displayservices.html",{'data':data})
def editservices(req,dataid):
    data=servicedb.objects.get(id=dataid)
    return render(req,"editservices.html",{'data':data})
def updateservice(req,dataid):
    if req.method=="POST":
        sn = req.POST.get('serv_name')
        pr = req.POST.get('Rates')
        ds=req.POST.get('ds')
        try:
            img = req.FILES['serv_photo']
            im = FileSystemStorage()
            file = im.save(img.name,img)
        except MultiValueDictKeyError:
            file=servicedb.objects.get(id=dataid).serv_photo
        servicedb.objects.filter(id=dataid).update(servicename=sn,rates=pr,serv_photo=file,description=ds)
        messages.success(req,"Data has been successfully updated")
        return redirect(displayservices)
def deleteservice(req,dataid):
    data=servicedb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"data successfully deleted")
    return redirect(displayservices)
def loginpage(req):
    return render(req,"adminlogin.html")
def loginsucces(req):
    if req.method=="POST":
        uname=req.POST.get("username")
        pswd=req.POST.get("pass")
        if User.objects.filter(username__contains=uname).exists():
            user=authenticate(username=uname,password=pswd)
            if user is not None:
                login(req,user)
                req.session['username']=uname
                req.session['password']=pswd
                return redirect(adminpage)
                messages.success(req,"login successfully")
            else:
                return redirect(loginpage)
            messages.error(req,"incorrect userid/password")
        else:
            return redirect(loginpage)
        messages.error(req,"incorrect userid or password")
def logoutuser(req):
    del req.session['username']
    del req.session['password']
    messages.success(req,"logout successfully")
    return redirect(loginpage)
def addmedicine(req):
    return render(req,"AddMedicines.html")
def savemedicine(req):
    if req.method=="POST":
        mn=req.POST.get('mname')
        cn=req.POST.get('cname')
        pr=req.POST.get('price')
        di=req.POST.get('descri')
        mp=req.FILES['mphoto']
        obj=medicinedb(medicinename=mn,companyname=cn,price=pr,description=di,photo=mp)
        obj.save()
        messages.success(req,"Data has been successfully saved")
        return redirect(addmedicine)
def displaymedicine(req):
    data=medicinedb.objects.all()
    return render(req,"displaymedicine.html",{'data':data})
def editmedicine(req,dataid):
    data=medicinedb.objects.get(id=dataid)
    return render(req,"editmedicine.html",{'data':data})
def updatemedicine(req,dataid):
    if req.method=="POST":
        mn = req.POST.get('mname')
        cn = req.POST.get('cname')
        pr = req.POST.get('price')
        di = req.POST.get('descri')
        try:
            img=req.FILES['photo']
            im=FileSystemStorage()
            file=im.save(img.name,img)
        except MultiValueDictKeyError:
            file=medicinedb.objects.get(id=dataid).photo
        medicinedb.objects.filter(id=dataid).update(medicinename=mn,companyname=cn,price=pr,description=di,photo=file)
        messages.success(req,"Data has been successfully updated")
        return redirect(displaymedicine)
def deletemedicine(req,dataid):
    data=medicinedb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"data successfully deleted")
    return redirect(displaymedicine)
def gallery(req):
    return render(req,"gallery.html")
def savegallery(req):
    if req.method=="POST":
        psn=req.POST.get('mname')
        descr=req.POST.get('descri')
        photo=req.FILES['mphoto']
        obj=gallerydb(photoshortname=psn,description=descr,photo=photo)
        obj.save()
        messages.success(req,"data has been successfully saved")
        return redirect(gallery)

def displaygallery(req):
    data=gallerydb.objects.all()
    return render(req,"displaygallery.html",{'data':data})
def editgallery(req,dataid):
    data=gallerydb.objects.get(id=dataid)
    return render(req,"editgallery.html",{'data':data})
def updategallery(req,dataid):
    if req.method=="POST":
        psn=req.POST.get('mname')
        descr = req.POST.get('descri')
        try:
            img = req.FILES['mphoto']
            im = FileSystemStorage()
            file = im.save(img.name,img)
        except MultiValueDictKeyError:
            file=gallerydb.objects.get(id=dataid).photo
        gallerydb.objects.filter(id=dataid).update(photoshortname=psn,description=descr,photo=file)
        messages.success(req,"Date has been successfully updated")
        return redirect(displaygallery)
def deletegallery(req,dataid):
    data=gallerydb.objects.get(id=dataid)
    data.delete()
    messages.success(req,"Data has been successfully deleted")
    return redirect(displaygallery)
def adddepartment(req):
    return render(req,"adddprtment.html")
def savedepartment(req):
    if req.method=="POST":
        dn=req.POST.get('dept')
        dp=req.POST.get('desc')
        dp2=req.POST.get('desc2')
        fe1=req.POST.get('Features1')
        fe2=req.POST.get('Features2')
        fe3=req.POST.get('Features3')
        fe4=req.POST.get('Features4')
        dd=req.FILES['dept_photo']
        obj=deptdb(deptname=dn,deptphoto=dd,description=dp,description2=dp2,feature1=fe1,feature2=fe2,features3=fe3,features4=fe4)
        obj.save()
        messages.success(req,"Data has been successfully saved")
        return redirect(adddepartment)
def displaydept(req):
    data=deptdb.objects.all()
    return render(req,"displaydept.html",{'data':data})
def editdept(req,dataid):
    data=deptdb.objects.get(id=dataid)
    return render(req,"editdept.html",{'data':data})
def updatedept(req,dataid):
    if req.method=="POST":
        dn = req.POST.get('dept')
        dp = req.POST.get('desc')
        dp2 = req.POST.get('desc2')
        fe1 = req.POST.get('Features1')
        fe2 = req.POST.get('Features2')
        fe3 = req.POST.get('Features3')
        fe4 = req.POST.get('Features4')
        try:
            img = req.FILES['photo']
            im = FileSystemStorage()
            file = im.save(img.name,img)
        except MultiValueDictKeyError:
            file=deptdb.objects.get(id=dataid).deptphoto
        deptdb.objects.filter(id=dataid).update(deptname=dn,deptphoto=file,description=dp,description2=dp2,feature1=fe1,feature2=fe2,features3=fe3,features4=fe4)
        messages.error(req,"something wrong")
        messages.success(req,"Data has been successfully updated")
        return redirect(displaydept)
def deletedept(req,dataid):
    data=deptdb.objects.get(id=dataid)
    data.delete()
    messages.success(req,"Data has been successfully deleted")
    return redirect(displaydept)
def displaycontact(req):
    data=contactdb.objects.all()
    return render(req,"displaycontact.html",{'data':data})
def deletecontact(req,dataid):
    data=contactdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Data has been successfully deleted")
    return redirect(displaycontact)
def displayappoitment(req):
    data=appointmntdb.objects.all()
    return render(req,"displayappoitment.html",{'data':data})
def deleteappoitment(req,dataid):
    data=appointmntdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Data has been successfully deleted")
    return redirect(displayappoitment)
def displayservice(req):
    data=servicebookdb.objects.all()
    return render(req,"displayservice.html",{'data':data})
def deletebookedservice(req,dataid):
    data=servicebookdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req,"Data has been successfully deleted")
    return redirect(displayservice)
def displayacceptorders(req):
    data=savedeldb.objects.all()
    return render(req,"deleteorders.html",{'data':data})
def deleteorders(req,dataid):
    if req.method=="POST":
        sn=req.POST.get('sername')
        da=req.POST.get("date")
        ti=req.POST.get('tym')
        fn=req.POST.get('fname')
        pho=req.POST.get('ph')
        ema=req.POST.get('em')
        mes=req.POST.get('mess')
        obj=savedeldb(servicename=sn,date=da,time=ti,patientname=fn,Mobilenumber=pho,emailid=ema,remarks=mes)
        obj.save()
    data = servicebookdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Data has been successfully accepted")
    return redirect(displayacceptorders)

def displayusers(req):
    data=registerdb.objects.all()
    return render(req,"displayusers.html",{'data':data})
def deleteusers(req,dataid):
    data=registerdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayusers,{'data':data})
def displaybookedappointment(req):
    data=savedelappointmentdb.objects.all()
    return render(req,"displaybookedappontment.html",{'data':data})
def saveanddelbookedappointmnet(req,dataid):
    if req.method=="POST":
        hn=req.POST.get('hosname')
        dn=req.POST.get('doctname')
        dept=req.POST.get('dept')
        Date=req.POST.get('date')
        time=req.POST.get('tym')
        pname=req.POST.get('patientname')
        phonenum=req.POST.get('phonenum')
        email=req.POST.get('email')
        remarks=req.POST.get('remarks')
        obj=savedelappointmentdb(Hospitalname=hn,DoctorName=dn,Department=dept,Date=Date,Time=time,patientname=pname,phonenumber=phonenum,email=email,remarks=remarks)
        obj.save()
    data =appointmntdb.objects.filter(id=dataid)
    data.delete()
    messages.success(req, "Data has been successfully accepted                              ")
    return redirect(displaybookedappointment)


