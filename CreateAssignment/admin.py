from django.contrib import admin
from . models import CreateLink, Instruction, Question, Profile, Student, SubQuestion, RandomNumber


admin.site.register(CreateLink)
admin.site.register(Instruction)
admin.site.register(Question)
admin.site.register(Profile)
admin.site.register(Student)
admin.site.register(SubQuestion)
admin.site.register(RandomNumber)