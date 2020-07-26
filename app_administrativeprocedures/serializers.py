from rest_framework import serializers
from app_administrativeprocedures import models

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = ('__all__')


class UniversityFacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UniversityFaculty
        fields = ('__all__')


class AdministrativeProceduresDenominationGlobalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdministrativeProceduresDenominationGlobal
        fields = ('__all__')


class AdministrativeProceduresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdministrativeProcedures
        fields = ('__all__')


class AdministrativeProceduresRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdministrativeProceduresRequest
        fields = ('__all__')