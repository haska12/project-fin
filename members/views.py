from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserforms ,SeriesForm,ExamensForm,coursForm,ModulesForm,AnnoncesForm
from .forms import EncadrementDesThesesForm,EncadrementDesLicenceForm,EncadrementDesMAasterForm
from .models import CoursModels,ExamensModels,SeriesModels,moduleModels,AnnoncesModels,tokenModels
from .models import EncadrementDesLicenceModels,EncadrementDesMAasterModels,EncadrementDesThesesModels,UserProfileModels
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import FileResponse
from django.http import HttpResponse,Http404
from .decorators import unauthenticated_user,allowed_users
from .helps import send_forget_password,message_send
import os
import uuid
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your views here.
import os
import openai


#--------------------
def Merge(dict1, dict2):
    return(dict2.update(dict1))
def list():
    obj1 =SeriesModels.objects.all()
    obj2=ExamensModels.objects.all()
    obj3=CoursModels.objects.all()
    obj4=moduleModels.objects.all()
    obj5=AnnoncesModels.objects.all()
    obj6=EncadrementDesLicenceModels.objects.all()
    obj7=EncadrementDesMAasterModels.objects.all()
    obj8=EncadrementDesThesesModels.objects.all()
    img1="said_tkatek"

    return {"mambre":obj1,
        "Examens":obj2,
        "cours":obj3,
        "modules":obj4,
        "Annonces":obj5,
        "Licence":obj6,
        "MAaster":obj7,
        "Theses":obj8,
        "img1":img1,
       
        }

     

@login_required(login_url="login")
def home_page(request,*args,**kwargs):
    my_context=list()
    a=request.user
    return render(request,"home.html",my_context)

@login_required(login_url="login")
def CV_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"Cv.html",my_context)

@unauthenticated_user
def login_views(request):
    
    if request.method == 'POST':
        usernam=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=usernam,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, "there was errour in login try again ... ")
    return render(request,"login.html",list())

def logout_User(request,*args,**kwargs):
    logout(request)
    return redirect('login')
from django.contrib import messages
@unauthenticated_user
def signup_views(request,*args,**kwargs):
    form= createUserforms()
    if request.method == 'POST':
        form= createUserforms(request.POST)

        if form.is_valid():
            user=form.save()
            username= form.cleaned_data.get('username')
            group=Group.objects.get(name='etudiants')
            user.groups.add(group)
            return redirect('login')
        else:
            messages.success(request, "there was errour in sign up try again ... ")
        
            
            
    cotexte={"form":form}

    cotexte.update(list())
    return render(request,"signup.html",cotexte)

@unauthenticated_user
def forget_password_veiws(request,*args,**kwargs):
    if request.method == 'POST':
        usernam=request.POST.get('username')
        try:
            user =User.objects.get(username=usernam)
            token=uuid.uuid4()
            try:
                token2=tokenModels.objects.get(iduser=user)
                token2.token=token
                token2.save()
                messages.success(request, "le lien a été envoyé ... ",extra_tags='success')
            except:
                form=tokenModels(iduser=user,token=token)
                form.save()
            messages.success(request, "le lien a été envoyé ... ",extra_tags='success')
        
            t=send_forget_password(user.email,token,user.id)
        except:
            txt="aucun utilisateur trouvé avec le nom d'utilisateur "+usernam+" ... "
            messages.error(request,txt ,extra_tags='error')

        
        
      
    return render(request,"forget_password.html",list())
from datetime import datetime
def Token_Link_expire(dateCreate):
    DateExpaire=datetime(dateCreate.year, dateCreate.month, dateCreate.day+3,0,0)
    Datenow=datetime.now()
    if DateExpaire < Datenow:
        print("expaire",dateCreate.year, dateCreate.month, dateCreate)
        return False
    print("not expaire")
    return True

@unauthenticated_user 
def rest_password_veiws(request,token,pk):
    
    user =User.objects.get(id=pk)

    try:
        token2=tokenModels.objects.get(iduser=user)
    except:
        return HttpResponse("<h1> expaire link </h1>")
    if not Token_Link_expire(token2.postdate):
        token2.delete()
        return HttpResponse("<h1> expaire link </h1>")

    if token2.token!=token:
        return HttpResponse("<h1> url not corecte </h1>")
    form=createUserforms(instance=user)
    if request.method == 'POST':
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2 and password1!= None:
            user.password=password1
            user.set_password(password1)
            user.save()
            token2.delete()
            messages.success(request, "changement de mot de passe réussi ... ",extra_tags='success')
            #return redirect('login')
        else:
            
            messages.error(request, "une erreur s'est produite lors de la connexion, essayez à nouveau... " ,extra_tags='error')

    cotexte={"form":form}
    cotexte.update(list())

    return render(request,"rest_password.html",cotexte)



#--------------------------------------------------------

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Series_Upload_views(request):
    form= SeriesForm()
    if request.method == 'POST':
        form= SeriesForm(request.POST,request.FILES)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('Series_Update')
    cotexte={"form":form}
    cotexte.update(list())
    return render(request,"SeriesUpload.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Series_Update_views(request):
    cotexte= list()
    return render(request,"SeriesUpdate.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Serie_Update_views(request,pk):
    obj =SeriesModels.objects.get(id=pk)
    form= SeriesForm(instance=obj)
    file_path=obj.file.path
    if request.method == 'POST':
        form= SeriesForm(request.POST,request.FILES,instance=obj)
        print(form.is_valid())
        if form.is_valid():
            if os.path.isfile(file_path):
                os.remove(file_path)
            form.save()
            return redirect('Series_Update_views')
    cotexte={"form":form}
    cotexte.update(list())
    return render(request,"SeriesUpload.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Series_delete_views(request,pk):
    
    obj =SeriesModels.objects.get(id=pk)
    file_path=obj.file.path
    if request.method == 'POST':
        
        try:
            if os.path.isfile(file_path):
                os.remove(file_path)
                obj.delete()
        except:
            print("file no found")
        
        return redirect("Series_Update")
    cotexte= {
        "Serie":obj
    }
   
    return render(request,"SerieDelete.html",cotexte)

#-----------------------------------
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Cours_Upload_views(request):
    form= coursForm()
    if request.method == 'POST':
        form= coursForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("cour_Update")
    cotexte={"form":form}
    cotexte.update(list())
    return render(request,"coursUpload.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def cours_Update_views(request):
    cotexte= list()
    
    return render(request,"coursUpdate.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def cour_Update_views(request,pk):
    obj= CoursModels.objects.get(id=pk)
    form= coursForm(instance=obj)
    file_path=obj.file.path
    if request.method == 'POST':
        form= SeriesForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            if os.path.isfile(file_path):
                os.remove(file_path)
            return redirect("cour_Update")
    cotexte={"form":form}
    cotexte.update(list())
    return render(request,"coursUpload.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def cour_Delete_views(request,pk):
    obj= CoursModels.objects.get(id=pk)
    file_path=obj.file.path
    if request.method == 'POST':
        if os.path.isfile(file_path):
                os.remove(file_path)
        obj.delete()
        return redirect("cour_Update")
              
    cotexte={"cour":obj}
    cotexte.update(list())
    return render(request,"courDelete.html",cotexte)
#----------------------------------
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Examens_Upload_views(request):
    form= ExamensForm()
    if request.method == 'POST':
        form= ExamensForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    cotexte={"form":form}
    cotexte.update(list())
    return render(request,"ExamensUpload.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Examens_Update_views(request):
    cotexte= list()
    return render(request,"ExamensUpdate.html",cotexte)


@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Examen_Update_views(request,pk):
    obj=ExamensModels.objects.get(id=pk)
    form=ExamensForm(instance=obj)
    file_path=obj.file.path
    if request.method == 'POST':
        form= ExamensForm(request.POST,request.FILES,instance=obj)
        if form.is_valid():
            form.save()
            if os.path.isfile(file_path):
                os.remove(file_path)
    cotexte={"form":form}
    cotexte.update(list())
    return render(request,"ExamensUpload.html",cotexte)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Examen_Delete_views(request,pk):
    obj=ExamensModels.objects.get(id=pk)
    file_path=obj.file.path
    if request.method == 'POST':
        obj.delete()
        if os.path.isfile(file_path):
             os.remove(file_path)  
        return redirect("Examens_Update")        
    cotexte={"Examen":obj}
    cotexte.update(list())
    return render(request,"ExamensDelete.html",cotexte)
#----------------------

def serie_pdf_view(request,pk):
    # Path to the PDF file
    obj =SeriesModels.objects.get(id=pk)
    pdf_path = obj.file.path
    # Read the PDF file
    with open(pdf_path, 'rb') as f:
        pdf = f.read()
    # Create a HttpResponse object with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="file.pdf"'
    return response

@login_required(login_url="login")

def Serie_display_views(request,pk):

    obj =SeriesModels.objects.get(id=pk)
    path=obj.file.path
    
    my_context={  "form":obj,"path":path}
    my_context.update(list())
    return render(request,"Series.html",my_context)

@login_required(login_url="login")
def cour_pdf_view(request,pk):
    # Path to the PDF file
    obj =CoursModels.objects.get(id=pk)
    pdf_path = obj.file.path
    # Read the PDF file
    with open(pdf_path, 'rb') as f:
        pdf = f.read()
    # Create a HttpResponse object with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="file.pdf"'
    return response

@login_required(login_url="login")
def Cour_display_views(request,pk):

    obj =CoursModels.objects.get(id=pk)
    my_context={    "form":obj }
    my_context.update(list())
    return render(request,"Cour.html",my_context)

@login_required(login_url="login")
def Examen_pdf_view(request,pk):
    # Path to the PDF file
    obj =ExamensModels.objects.get(id=pk)
    pdf_path = obj.file.path
    # Read the PDF file
    with open(pdf_path, 'rb') as f:
        pdf = f.read()
    # Create a HttpResponse object with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="file.pdf"'
    return response

@login_required(login_url="login")
def Examen_display_views(request,pk):

    obj =ExamensModels.objects.get(id=pk)
    my_context={ "form":obj}
    my_context.update(list())
    return render(request,"Examen.html",my_context)

def img_pdf_view(request):
    # Path to the PDF file

    pdf_path = "templet\static\stkat.png"
    # Read the PDF file
    with open(pdf_path, 'rb') as f:
        pdf = f.read()
    # Create a HttpResponse object with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="file.pdf"'
    return response
def logo_img_pdf_view(request):
    # Path to the PDF file
    pdf_path = "templet\static\logo1.png"
    # Read the PDF file
    with open(pdf_path, 'rb') as f:
        pdf = f.read()
    # Create a HttpResponse object with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="file.pdf"'
    return response

def img_pdf_view_all(request):
    # Path to the PDF file
  
    pdf_path = "templet\static\img1.jpg"
    # Read the PDF file
    with open(pdf_path, 'rb') as f:
        pdf = f.read()
    # Create a HttpResponse object with the PDF content
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="file.pdf"'
    return response
    
    
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Modules_views(request):
    form= ModulesForm()
    if request.method == 'POST':
        form= ModulesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Serie_Update')

    cotexte=list()
    return render(request,"Modules.html",cotexte)


@login_required(login_url="login")
def Modules_despay_views(request,nom):
    obj = moduleModels.objects.get(modulenom=nom)
    my_context={ "form":obj}
    my_context.update(list())
    return render(request,"ModulseDisplay.html",my_context)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Modules_upload_views(request):
    form =ModulesForm()
    if request.method == 'POST':
        form= ModulesForm(request.POST)
 
        if form.is_valid():
            form.save()
            return redirect('Modules_views')

    my_context={ "form":form}
    my_context.update(list())
    return render(request,"modulesupload.html",my_context)

@allowed_users(Allowed_roles=['admin','professeure'])
def Modules_update_views(request,nom):
    obj = moduleModels.objects.get(modulenom=nom)

    form =ModulesForm(instance=obj)
    if request.method =='POST':
        
        form =ModulesForm(request.POST,instance=obj)
       
        if form.is_valid():
            form.save()
            if request.POST.get('modulenom')!=moduleModels.objects.get(modulenom=nom):
                moduleModels.objects.get(modulenom=nom).delete()
            return redirect('Modules_views') 

    my_context={"form":form}
    my_context.update(list())
    return render(request,"modulesupload.html",my_context)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Modules_delete_views(request,nom):
    obj = moduleModels.objects.get(modulenom=nom)
    obj2 =SeriesModels.objects.filter(module=nom)
    obj3=ExamensModels.objects.filter(module=nom)
    obj4=CoursModels.objects.filter(module=nom)
    obj3.delete()
    obj4.delete()
    obj2.delete()
    obj.delete()
    return redirect('Modules_views') 



@login_required(login_url="login")
def  Annonces_despleye_views(request):
    my_context=list()
    return render(request,"Annonces.html",my_context)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Annonces_uplod_views(request):
    form= AnnoncesForm()
    if request.method == 'POST':
        form= AnnoncesForm(request.POST)

        print(form.is_valid())
        if form.is_valid():
            form.save()
        else:
            print(6)
    my_context={"form":form}
    my_context.update(list())
    return render(request,"AnnoncesUplode.html",my_context)


def Annonce_uplod_views(request,name):
    
    obj=AnnoncesModels.objects.get(name=name)
    my_context={"form":obj}
    my_context.update(list())
    return render(request,"Annonce.html",my_context)


@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def  Annonces_views(request):
    my_context=list()
    return render(request,"AnnoncesUpdate.html",my_context)
@allowed_users(Allowed_roles=['admin','professeure'])
def Annonce_delete_views(request,):
    obj=AnnoncesModels.objects.get(name=name)
    obj.delete()
    return redirect("Annonces_uplod")

@allowed_users(Allowed_roles=['admin','professeure'])
@login_required(login_url="login")
def Annonces_update_views(request,name):
    obj=AnnoncesModels.objects.get(name=name)
    
    form= AnnoncesForm(instance=obj)
    if request.method == 'POST':
        form= AnnoncesForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect("home")
    my_context={"form":form}
    my_context.update(list())
    return render(request,"AnnoncesUplode.html",my_context)



#---------------------------------------------------**********************
@login_required(login_url="login")
def Contact_page(request,*args,**kwargs):
    if request.method == 'POST':
        FirstName=request.POST.get('FirstName')
        LasteName=request.POST.get('LasteName')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        messge=request.POST.get('message')
        print(messge)
        print(message_send(email,subject,messge))

    my_context=list()
    return render(request,"Contact.html",my_context)




@login_required(login_url="login")
def These_desplay_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"EncadrementDesThesesdesplay.html",my_context)
#EncadrementDesThesesupdate

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def These_update_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"EncadrementDesThesesupdate.html",my_context)
#EncadrementDesThesesupload
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def These_uplod_views(request):
    form=EncadrementDesThesesForm()
    if request.method == 'POST':
        form= EncadrementDesThesesForm(request.POST,)

        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('These_update_page')
    my_context={"form":form}
    my_context.update(list())
    return render(request,"EncadrementDesThesesupload.html",my_context)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def These_delete_views(request,pk):
    obj=EncadrementDesThesesModels.objects.get(id=pk)
    print(obj)
    obj.delete()
    return redirect('These_update_page')

#-----------------------------------------------------

#EncadrementDesLicenceDesplaye
@login_required(login_url="login")
def Licence_desplay_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"EncadrementDesLicenceDesplaye.html",my_context)
#EncadrementDesLicenceUpdate
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Licence_update_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"EncadrementDesLicenceUpdate.html",my_context)
#EncadrementDesLicenceUpload
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Licence_upload_views(request):
    form=EncadrementDesLicenceForm()
    if request.method == 'POST':
        form= EncadrementDesLicenceForm(request.POST,)

        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('Licence_update_page')
    my_context={"form":form}
    my_context.update(list())
    return render(request,"EncadrementDesLicenceUpload.html",my_context)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def Licence_delete_views(request,pk):
    obj=EncadrementDesLicenceModels.objects.get(id=pk)
    print(obj)
    obj.delete()
    return redirect('Licence_update_page')


#------------------------------------------------
#EncadrementDesMAasterModelsDdesplaye
@login_required(login_url="login")
def MAaster_desplay_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"EncadrementDesMAasterModelsDdesplaye.html",my_context)
#EncadrementDesMAasterUpdate
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def MAaster_update_page(request,*args,**kwargs):
    my_context=list()
    return render(request,"EncadrementDesMAasterUpdate.html",my_context)
#EncadrementDesMAasterupoad
@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def MAaster_upload_views(request):
    form=EncadrementDesMAasterForm()
    if request.method == 'POST':
        form= EncadrementDesMAasterForm(request.POST,)

        print(form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('MAaster_update_page')
    my_context={"form":form}
    my_context.update(list())
    return render(request,"EncadrementDesMAasterupoad.html",my_context)

@login_required(login_url="login")
@allowed_users(Allowed_roles=['admin','professeure'])
def MAaster_delete_views(request,pk):
    obj=EncadrementDesMAasterModels.objects.get(id=pk)
    obj.delete()
    return redirect('MAaster_update_page')




    
# ////
def PUBLICATION_SCIENTIFIQUE_viewa(request):
    my_context=list()
    return render(request,"PUBLICATIONSCIENTIFIQUE.html",my_context)