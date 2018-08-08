from django.contrib import admin
from .models import MOU,Student
# Register your models here.
class publicAdmin(admin.ModelAdmin):
	list_display=[f.name for f in MOU._meta.fields]
admin.site.register(MOU,publicAdmin)

class studentAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Student._meta.fields]
admin.site.register(Student,studentAdmin)
