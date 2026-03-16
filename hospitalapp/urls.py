
from django.contrib import admin
from django.urls import path
from hospitalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home, name = 'home'),

    path('starter/', views.starter, name = 'starter'),

    path('about/', views.about, name = 'about'),

    path('appointment/', views.appointment, name = 'appointment'),

    path('contact/', views.contact, name = 'contact'),

    path('services', views.services, name = 'services'),

    path('departments', views.departments, name = 'departments'),

    path('doctors', views.doctors, name= 'doctors'),

    path('show/', views.show, name = 'show'),

    path('patients/', views.showpatient, name = 'patients'),

    path('delete/<int:id>/', views.delete),

    path('edit/<int:id>/', views.edit),

    path('', views.register, name = 'register'),

    path('login/', views.login_user, name = 'login'),

    #Mpesa API

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),
    path('transactions/', views.transactions_list, name='transactions'),

]
