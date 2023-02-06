# from django.contrib import admin
from django.urls import path
from .views import About,Home,Contact,Index,Login,Logout_admin,View_Doctor,Delete_Doctor,Add_Doctor

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', Home, name='home'),
    path('about/', About, name='about'),
    path('contact/', Contact, name='contact'),
    path('admin_login/', Login, name='admin_login'),
    path('logout/', Logout_admin, name='logout_admin'),
    path('index/', Index, name='dashboard'),
    path('view_doctor/', View_Doctor, name='view_doctor'),
    path('add_doctor/', Add_Doctor, name='add_doctor'),
    path('delete_doctor(?p<int:pid>)/', Delete_Doctor, name='delete_doctor'),

]
