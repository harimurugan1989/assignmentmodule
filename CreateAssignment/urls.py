from os import link
from django.contrib import admin
from django.urls import path

from CreateAssignment.views.assignmentsummary import asummary
from .views import *

urlpatterns = [
    path('register/',Register,name='CreateAssignment-register'), 
    path('login/',DoLogin,name='CreateAssignment-login'),
    path('logout/',DoLogout,name='CreateAssignment-logout'),
    path('<slug:link>/instructions/',Instructions,name='CreateAssignment-instructions'),
    path('<slug:link>/', Summary,name='CreateAssignment-summary'),
    path('create',LinkCreate,name='CreateAssignment-home'),
    path('',asummary,name='Summary-Assignment'),     
    path('<slug:link>/edit/',LinkEdit ,name='CreateAssignment-edit'),
    path('<slug:link>/edit/deletelink/',LinkEdit,name='CreateAssignment-deletelink'),
    path('<slug:link>/questions/',QuestionAdd ,name='CreateAssignment-questions'),
    path('<slug:link>/edit_question/<int:qno>/addsubquestion',SubQuestionAdd ,name='SubQuestionAdd'),
    path('<slug:link>/edit_question/<int:qno>/savequestion',SubQuestionSave ,name='SubQuestionAdd'),
    path('<slug:link>/edit_question/<int:qno>/',QuestionEdit ,name='CreateAssignment-edit_question'),
    path('<slug:link>/edit_question/<int:qno>/add-text-box',QuestionAddTextbox ,name='add-question-textbox'),
    path('<slug:link>/edit_question/<int:qno>/add-image-question',QuestionAddImage ,name='add-question-image'),
    path('<slug:link>/edit_question/<int:qno>/delete-it',QuestionDeleteBox ,name='add-question-image'),
    path('<slug:link>/delete_question/<int:qno>/',QuestionDelete ,name='CreateAssignment-delete_question'),
    path('<slug:link>/assignment/',TakeAssignment,name='CreateAssignment-assignment'),
]