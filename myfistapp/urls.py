"""myfistapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from members.views import home_page,login_views,signup_views,logout_User,Series_Upload_views
from members.views import Cours_Upload_views,Examens_Upload_views,Serie_display_views,Cour_display_views,Examen_display_views,Modules_views
from members.views import serie_pdf_view,cour_pdf_view,Examen_pdf_view,img_pdf_view
from members.views import Series_Update_views,cours_Update_views, Examens_Update_views
from members.views import Serie_Update_views,cour_Update_views,Examen_Update_views
from members .views import Series_delete_views,cour_Delete_views,Examen_Delete_views,CV_page
from members.views import Modules_despay_views,Modules_upload_views,Modules_update_views,Modules_delete_views
from members.views import Annonces_despleye_views,Annonces_uplod_views,Annonce_uplod_views,Annonces_views,Annonce_delete_views,Annonces_update_views
from members.views import  Contact_page
from members.views import These_desplay_page,These_update_page,These_uplod_views,These_delete_views
from members.views import Licence_desplay_page,Licence_update_page,Licence_upload_views,Licence_delete_views
from members.views import MAaster_desplay_page,MAaster_update_page,MAaster_upload_views,MAaster_delete_views
from members.views import forget_password_veiws,rest_password_veiws
from members.views import logo_img_pdf_view,chat_bot_wiews

urlpatterns = [

    path('admin/', admin.site.urls),
    
    path('home/',home_page,name='home'),
    path('cv/',CV_page,name='CV'),
    path('login/',login_views,name='login'),
    path('signup/',signup_views,name='signup'),
    path('logout/',logout_User,name='logoutUser'),
    path('logout/',logout_User,name='logoutUser'),
     path('forget_password/',forget_password_veiws,name='forget_password'),
      path('rest_password/<str:token>/<str:pk>/',rest_password_veiws,name='rest_password_veiws'),
   path('logo_img_pdf_view/',logo_img_pdf_view,name='logo_img_pdf_view'),
path('chat_bot_wiews/',chat_bot_wiews,name='chat_bot_wiews'),

    path('Series_Upload/',Series_Upload_views,name='SeriesUpload'),
    path('Cours_Upload/',Cours_Upload_views,name='CoursUpload'),
    path('Examens_Upload/',Examens_Upload_views,name='ExamensUpload'),
    path('Series/<str:pk>/',Serie_display_views,name='Seriesdisplay'),
    path('Examen/<str:pk>/',Examen_display_views,name='Examendisplay'),
    path('cour/<str:pk>/',Cour_display_views,name='Courdisplay'),
    path('pdf_serie/<str:pk>/', serie_pdf_view, name='serie_pdf_view'),
    path('pdf_cour/<str:pk>/', cour_pdf_view, name='cour_pdf_view'),
    path('pdf_Examen/<str:pk>/', Examen_pdf_view, name='Examen_pdf_view'),
    path('img_pdf_view/', img_pdf_view, name='img_pdf_view'),
    path('Series_Update_views/',Series_Update_views,name='Series_Update'),
     path('cours_Update_views/',cours_Update_views,name='cour_Update'),
      path('Examens_Update_views/',Examens_Update_views,name='Examens_Update'),
    path('Serie_Update_views/<str:pk>/',Serie_Update_views,name='Serie_Update'),
   path('cour_Update_views/<str:pk>/',cour_Update_views,name='cour_Update'),
    path('Examens_Update_views/<str:pk>/',Examen_Update_views,name='Examen_Update'),
     path('Series_delete_views/<str:pk>/',Series_delete_views,name='Series_delete'),
    path('cour_Delete_views/<str:pk>/',cour_Delete_views,name='cour_Delete'),
        path('Examen_Delete_views/<str:pk>/',Examen_Delete_views,name='Examen_Delete'),
       
           path('Modules_views/',Modules_views,name='Modules_views'),
         path('Modules_despay_views/<str:nom>/',Modules_despay_views,name='Modules_despay_views'),
        path('Modules_upload/',Modules_upload_views,name='Modules_upload'),
           path('Modules_update_views/<str:nom>/',Modules_update_views,name='Modules_update_views'),
path('Modules_delete_views/<str:nom>/',Modules_delete_views,name='Modules_delete_views'),

path('Annonces_despleye/',Annonces_despleye_views,name="Annonces_despleye"),
path('Annonces_uplod/',Annonces_uplod_views,name="Annonces_uplod"),
path('Annonce_uplod/<str:name>/',Annonce_uplod_views,name="Annonce_uplod"),
path('Annonces_views/',Annonces_views,name="Annonces_views"),
path('Annonce_delete/<str:name>/',Annonce_delete_views,name="Annonce_delete"),
path('Annonces_update/<str:name>/',Annonces_update_views,name="Annonces_update_views"),

path('Contact_page/',Contact_page,name="Contact_page"),

path('These_desplay_page/',These_desplay_page,name="These_desplay_page"),
path('These_update_page/',These_update_page,name="These_update_page"),
path('These_uplod_views/',These_uplod_views,name="These_uplod_views"),
path('These_delete_views/<str:pk>/',These_delete_views,name="These_delete_views"),


path('Licence_desplay_page/',Licence_desplay_page,name="Licence_desplay_page"),
path('Licence_update_page/',Licence_update_page,name="Licence_update_page"),
path('Licence_upload/',Licence_upload_views,name="Licence_upload_views"),
path('Licence_delete/<str:pk>/',Licence_delete_views,name="Licence_delete_views"),


path('MAaster_desplay_page/',MAaster_desplay_page,name="MAaster_desplay_page"),
path('MAaster_update/',MAaster_update_page,name="MAaster_update_page"),
path('MAaster_upload/',MAaster_upload_views,name="MAaster_upload_views"),
path('MAaster_delete/<str:pk>/',MAaster_delete_views,name="MAaster_delete_views"),
]
