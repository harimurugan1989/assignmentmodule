from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.linkcreate,name='CreateAssignment-home'),
    path('register/', views.register,name='register'),
    path('login/', views.do_login,name='login'),



    path('<slug:link>/assignment/',views.student_view,name='CreateAssignment-student'),
    path('<slug:link>/instructions/',views.instruct,name='CreateAssignment-instructions'),
    path('<slug:link>/addquestion/',views.addquestion,name='CreateAssignment-addquestion'),
    path('<slug:link>/editquestion/<int:qno>',views.editquestion,name='CreateAssignment-editquestion'),
    path('<slug:link>/deletequestion/<int:nu>',views.deletequestion,name='CreateAssignment-deletequestion'),
    path('<slug:link>/',views.summary,name='CreateAssignment-summary'),
    path('<slug:link>/settings/',views.settings,name='settings'),
    path('<slug:link>/deletelink/',views.deletelink,name='deletelink'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)