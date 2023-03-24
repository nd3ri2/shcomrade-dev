from . import views
from django.urls import path

app_name = 'core'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrees', views.register, name='register'),
    path('investments', views.investments, name='investments'),
    path('s', views.reg_success, name='reg_success'),
    path('member/<slug:member_number>/', views.member, name='member'),

]
