from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Company)
admin.site.register(Skills)
admin.site.register(user_data)
admin.site.register(Education)
admin.site.register(Certifications)

