from django.urls import  path
from.import views
from django.conf.urls.static import static,settings

urlpatterns = [
    path('', views.home, name='home'),
    #path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('request_blood/', views.request_blood, name='requestblood'),
    path('profile/', views.profile, name='profile'),
    path('profile/editprofile',views.edit_profile,name='editprofile'),
    path('requests/', views.request_blood_list, name='requests'),
    path('request_blood/success', views.sucess_page, name='success'),
   

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    