from django.contrib import admin
from .models import SeriesModels,CoursModels,ExamensModels,moduleModels,moduleModels,AnnoncesModels
from .models import EncadrementDesLicenceModels,EncadrementDesMAasterModels,EncadrementDesThesesModels,tokenModels
from .models import UserProfileModels

# Register your models here.
admin.site.register(SeriesModels)
admin.site.register(CoursModels)
admin.site.register(ExamensModels)
admin.site.register(moduleModels)
admin.site.register(AnnoncesModels)
admin.site.register(EncadrementDesLicenceModels)
admin.site.register(EncadrementDesThesesModels)
admin.site.register(EncadrementDesMAasterModels)
admin.site.register(tokenModels)
admin.site.register(UserProfileModels)
