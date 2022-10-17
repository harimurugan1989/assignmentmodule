from os import link
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.linkcreate,name='CreateAssignment-home'),

    path('register/',views.register,name='CreateAssignment-register'),

    path('login/',views.do_login,name='CreateAssignment-login'),

    path('logout/',views.do_logout,name='CreateAssignment-logout'),

    path('<slug:link>/instructions/',views.instructions,name='CreateAssignment-instructions'),

    path('<slug:link>/', views.summary,name='CreateAssignment-summary'),

    path('<slug:link>/edit/',views.edit ,name='CreateAssignment-edit'),

    path('<slug:link>/edit/deletelink/',views.linkdelete ,name='CreateAssignment-deletelink'),

    path('<slug:link>/questions/',views.questions ,name='CreateAssignment-questions'),

    path('<slug:link>/edit_question/<int:qno>/',views.edit_question ,name='CreateAssignment-edit_question'),

    path('<slug:link>/delete_question/<int:qno>/',views.delete_question ,name='CreateAssignment-delete_question'),

    path('<slug:link>/assignment/',views.take_assignment,name='CreateAssignment-assignment'),
]