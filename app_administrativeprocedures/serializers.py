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

class AdministrativeProceduresRequestAskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdministrativeProceduresRequest
        fields = ('description',
                  'code_bank',
                  'payment')

class AdministrativeProceduresAskSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        data = super(AdministrativeProceduresAskSerializer, self).to_representation(instance)
        data['unidad'] = instance.denomination_global.unit.name
        data['denomination_global'] = instance.denomination_global.name
        requisitos = models.AdministrativeProceduresRequest.objects.filter(administration_procedures=instance)
        data['requisitos'] = (AdministrativeProceduresRequestAskSerializer(requisitos, many=True)).data
        return data

    class Meta:
        model = models.AdministrativeProcedures
        fields = ('denomination',
                  'code_bank',
                  'payment')
