from django.contrib import admin
from app_administrativeprocedures import models

# Register your models here.
admin.site.register(models.Unit)
admin.site.register(models.UniversityFaculty)
admin.site.register(models.AdministrativeProceduresDenominationGlobal)
admin.site.register(models.AdministrativeProcedures)
admin.site.register(models.AdministrativeProceduresRequest)