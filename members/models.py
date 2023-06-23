from django.db import models
from django.contrib.auth.models import Group, Permission,User
import django.contrib.auth.models
from django.utils import timezone


# Create your models here.
try:
  group1=Group.objects.get(name='professeure' )
except:
   group1 = Group.objects.create(name='professeure',permissions=all)
try:
  group1=Group.objects.get(name='admin')
except:
   group1 = Group.objects.create(name='admin',permissions=all)
try:
  group2=Group.objects.get(name='etudiants')
except:
   group2 = Group.objects.create(name='etudiants')

try:
  user=User.objects.get(username='said tkatek')
except:
   user =User.objects.create(username='said tkatek', email='saidtkatek@gmail.com',first_name='said',last_name='tkatek',password='Qwert1234',is_staff=True,is_superuser=True)
  
try:
    user.groups.add(group1)
except:
    print("error")


class UserProfileModels(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    backgroundColorType=models.CharField(max_length=100, blank=False, null=False,default='normele')     
    
       

class tokenModels(models.Model):
    iduser =models.OneToOneField(User, on_delete=models.CASCADE)
    postdate =models.DateField( null=True, blank=True)
    token=models.CharField(max_length=100)
    def save(self):
        if not self.id:
            self.postdate = timezone.now()
        super(tokenModels, self).save()

class moduleModels(models.Model):
    modulenom =  models.CharField(max_length= 55, blank=False, null=False,default="module" ,unique=True ,primary_key=True  )
    def __repr__(self):
        return 'Resume(%s)' % (self.modulenom)
    def __str__ (self):
        return self.modulenom

class SeriesModels(models.Model):
    module=models.ForeignKey(moduleModels, on_delete=models.CASCADE, null=True)
    
    name = models.CharField(max_length= 55, blank=False, null=False,default="Series")
    file = models.FileField(upload_to= 'templet/files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name
    
class ExamensModels(models.Model):
    module=models.ForeignKey(moduleModels, on_delete=models.CASCADE, null=True)
  
    name = models.CharField(max_length= 55, blank=False, null=False,default="examen")
    file = models.FileField(upload_to= 'templet/files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name
class CoursModels(models.Model):
    module=models.ForeignKey(moduleModels, on_delete=models.CASCADE, null=True)
   
    name = models.CharField(max_length= 55, blank=False, null=False,default="chapitre")
    file = models.FileField(upload_to= 'templet/files/',null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

    def __str__ (self):
        return self.name




class AnnoncesModels(models.Model):
    name = models.CharField(max_length= 100, blank=False, null=False,default="title" ,unique=True)
    postdate =models.DateField( null=True, blank=True)
    updated =models.DateField(null=True, blank=True)
    text  =models.CharField(max_length= 1000 )
    link =models.CharField(max_length= 100 ,blank=False, null=False,default="#" )
    def __repr__(self):
        return 'Resume(%s)' % (self.name)
    def __str__ (self):
        return self.name
    def save(self):
        if not self.id:
            self.postdate = timezone.now()
            
        self.updated = timezone.now()
        super(AnnoncesModels, self).save()

class EncadrementDesThesesModels(models.Model):
    Doctorant = models.CharField(max_length= 50, blank=False, null=False,default="#" ,unique=True)
    Sujet  =models.CharField(max_length= 700 )
    AnneeInscription =models.CharField(max_length= 100 ,blank=False, null=False,default="#" )

    def __repr__(self):
        return 'Resume(%s)' % (self.Doctorant)
    def __str__ (self):
        return self.Doctorant

    
class EncadrementDesMAasterModels(models.Model):
    name = models.CharField(max_length= 100, blank=False, null=False,default="nom" ,unique=True)
    SujetsDesPFE=models.CharField(max_length= 700 )
    AnneeInscription= models.CharField(max_length= 100 ,blank=False, null=False,default="(2019-2021)" )
    def __repr__(self):
        return 'Resume(%s)' % (self.name)
    def __str__ (self):
        return self.name

class EncadrementDesLicenceModels(models.Model):
    SujetsDesPFE=models.CharField(max_length= 700 )
    EtudiantsConcernes= models.CharField(max_length= 100 ,blank=False, null=False,default="#" )
    Filiere=models.CharField(max_length= 50 ,blank=False, null=False,default="(SMI S6) 2020/2021")
    def __repr__(self):
        return 'Resume(%s)' % (self.EtudiantsConcernes)
    def __str__ (self):
        return self.EtudiantsConcernes