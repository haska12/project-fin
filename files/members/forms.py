from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import SeriesModels,ExamensModels,CoursModels,moduleModels,AnnoncesModels
from .models import EncadrementDesLicenceModels,EncadrementDesMAasterModels,EncadrementDesThesesModels


class createUserforms(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class SeriesForm(forms.ModelForm):
   class Meta:
      model = SeriesModels
      fields = ['name','file','module']
      
class coursForm(forms.ModelForm):
   class Meta:
      model = CoursModels
      fields = ['name','file','module']
class ExamensForm(forms.ModelForm):
   class Meta:
      model = ExamensModels
      fields = ['name','file','module']
class ModulesForm(forms.ModelForm):
   class Meta:
      model = moduleModels
      fields = ['modulenom']

class AnnoncesForm(forms.ModelForm):
   class Meta:
      model=AnnoncesModels
      fields=['name','postdate','text','link']

class EncadrementDesThesesForm(forms.ModelForm):
   class Meta:
      model=EncadrementDesThesesModels
      fields=['Doctorant','Sujet','AnneeInscription']

class EncadrementDesLicenceForm(forms.ModelForm):
   class Meta:
      model=EncadrementDesLicenceModels
      fields=['SujetsDesPFE','EtudiantsConcernes','Filiere']

class EncadrementDesMAasterForm(forms.ModelForm):
   class Meta:
      model=EncadrementDesMAasterModels
      fields=['name','SujetsDesPFE','AnneeInscription']
      