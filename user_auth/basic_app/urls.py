from django.urls import path
from . import views

app_name = 'basic_app'
urlpatterns = [
        path('', views.index, name='index'),
        path('other/', views.other, name='other'),
        path('register/', views.reg_form, name='register'),
        path('login/', views.user_login, name='login'),
        path('logout/', views.user_logout, name='logout'),

]
