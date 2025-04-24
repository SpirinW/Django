from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main-page'),
    path('1/', views.second_view, name='second-view'),
    path('2/', views.third_view, name='third-view'),
    path('3/', views.fourth_view, name='fourth-view'),
    path('4/', views.fifth_view, name='fifth-view'),
    path('5/', views.sixth_view, name='sixth-view'),
    path('page/about/', views.about_view, name='about'), 
]
