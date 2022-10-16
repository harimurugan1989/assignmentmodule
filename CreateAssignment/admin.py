from django.contrib import admin
from . models import createlink
from . models import instructions
from . models import questiondata
# from . models import assignquestion
from . models import Profile
from .models import *
# from . models import quest
admin.site.register(createlink)
admin.site.register(instructions)
admin.site.register(questiondata)
# admin.site.register(assignquestion)
admin.site.register(Profile)