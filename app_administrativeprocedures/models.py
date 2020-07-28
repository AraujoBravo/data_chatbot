from django.db import models

# Create your models here.
class Unit(models.Model):
    id_unit = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'unit'

    def __str__(self):
        return "{0}".format(self.name)


class UniversityFaculty(models.Model):
    id_universtityfaculty = models.AutoField(primary_key=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=False, blank=False)

    code = models.CharField(max_length=4, unique=True, null=False, blank=False)
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)

    class Meta:
        db_table = 'university_faculty'

    def __str__(self):
        return "{0}".format(self.name)


class AdministrativeProceduresDenominationGlobal(models.Model):
    id_denominationglobal = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, unique=True, null=False, blank=False)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        db_table = 'administrative_procedures_denomination_global'

    def __str__(self):
        return "{1}-{0}".format(self.name, self.unit)


class AdministrativeProcedures(models.Model):
    id_administrativeprocedures = models.AutoField(primary_key=True)
    denomination = models.CharField(max_length=200, null=False, blank=False)
    code_bank = models.CharField(max_length=10, null=False, blank=False)
    payment = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    denomination_global = models.ForeignKey('AdministrativeProceduresDenominationGlobal', on_delete=models.CASCADE,
                                            null=False, blank=False)

    class Meta:
        db_table = 'administrative_procedures'

    def __str__(self):
        return "{1}-{0}".format(self.denomination, self.denomination_global)


class AdministrativeProceduresRequest(models.Model):
    id_request = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300)
    code_bank = models.CharField(max_length=10, null=True, blank=True)
    payment = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    administration_procedures = models.ForeignKey('AdministrativeProcedures', on_delete=models.CASCADE, null=False,
                                                  blank=False)

    class Meta:
        db_table = 'administrative_procedures_request'

    def __str__(self):
        return "{0}".format(self.description)
