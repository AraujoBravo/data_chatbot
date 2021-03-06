from django.shortcuts import render
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app_administrativeprocedures import models, serializers
import unidecode

class AskChatBot(APIView):
    model_class = models.AdministrativeProcedures
    serializer_class = serializers.AdministrativeProceduresAskSerializer

    def get(self, request):
        unidad = request.data['unidad']
        denominacion = request.data['denominacion']
        # quitando tildes si hubieran
        unidad = unidecode.unidecode(unidad)
        denominacion = unidecode.unidecode(denominacion)
        model_object = self.model_class.objects.filter(Q(denomination_global__unit__name__icontains=unidad),
                                                       Q(denomination_global__name__icontains=denominacion) |
                                                       Q(denomination__icontains=denominacion))
        if model_object.exists():
            serializer_object = self.serializer_class(model_object, many=True)
            data = {
                'message': "Ejecutado con éxito",
                'status': "success",
                'status_code': status.HTTP_200_OK,
                'data': serializer_object.data
            }
        else:
            data = {
                'message': "No encontrado",
                'status': "error",
                'status_code': status.HTTP_200_OK,
            }
        return Response(data)


class Unit(APIView):
    model_class = models.Unit
    serializer_class = serializers.UnitSerializer

    def get(self, request):
        model_object = self.model_class.objects.all()
        serializer_object = self.serializer_class(model_object, many=True)
        data = {
            'message': "Ejecutado con éxito",
            'status': "success",
            'status_code': status.HTTP_200_OK,
            'data': serializer_object.data
        }
        return Response(data)

    def post(self, request):
        serializer_object = self.serializer_class(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            data = {
                'message': "Ejecutado con éxito",
                'status': "success",
                'status_code': status.HTTP_201_CREATED,
                'data': serializer_object.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message': "Error al ejecutar",
                'status': "error",
                'status_code': status.HTTP_400_BAD_REQUEST,
                'data': serializer_object.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UniversityFaculty(APIView):
    model_class = models.UniversityFaculty
    serializer_class = serializers.UniversityFacultySerializer

    def get(self, request):
        model_object = self.model_class.objects.all()
        serializer_object = self.serializer_class(model_object, many=True)
        data = {
            'message': "Ejecutado con éxito",
            'status': "success",
            'status_code': status.HTTP_200_OK,
            'data': serializer_object.data
        }
        return Response(data)

    def post(self, request):
        serializer_object = self.serializer_class(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            data = {
                'message': "Ejecutado con éxito",
                'status': "success",
                'status_code': status.HTTP_201_CREATED,
                'data': serializer_object.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message': "Error al ejecutar",
                'status': "error",
                'status_code': status.HTTP_400_BAD_REQUEST,
                'data': serializer_object.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class AdministrativeProceduresDenominationGlobal(APIView):
    model_class = models.AdministrativeProceduresDenominationGlobal
    serializer_class = serializers.AdministrativeProceduresDenominationGlobalSerializer

    def get(self, request):
        model_object = self.model_class.objects.all()
        serializer_object = self.serializer_class(model_object, many=True)
        data = {
            'message': "Ejecutado con éxito",
            'status': "success",
            'status_code': status.HTTP_200_OK,
            'data': serializer_object.data
        }
        return Response(data)

    def post(self, request):
        serializer_object = self.serializer_class(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            data = {
                'message': "Ejecutado con éxito",
                'status': "success",
                'status_code': status.HTTP_201_CREATED,
                'data': serializer_object.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message': "Error al ejecutar",
                'status': "error",
                'status_code': status.HTTP_400_BAD_REQUEST,
                'data': serializer_object.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class AdministrativeProcedures(APIView):
    model_class = models.AdministrativeProcedures
    serializer_class = serializers.AdministrativeProceduresSerializer

    def get(self, request):
        model_object = self.model_class.objects.all()
        for model in model_object:
            print(model.denomination)
            model.denomination = unidecode.unidecode(model.denomination)
            model.save()
            print(model.denomination)
        serializer_object = self.serializer_class(model_object, many=True)
        data = {
            'message': "Ejecutado con éxito",
            'status': "success",
            'status_code': status.HTTP_200_OK,
            'data': serializer_object.data
        }
        return Response(data)

    def post(self, request):
        serializer_object = self.serializer_class(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            data = {
                'message': "Ejecutado con éxito",
                'status': "success",
                'status_code': status.HTTP_201_CREATED,
                'data': serializer_object.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message': "Error al ejecutar",
                'status': "error",
                'status_code': status.HTTP_400_BAD_REQUEST,
                'data': serializer_object.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class AdministrativeProceduresRequest(APIView):
    model_class = models.AdministrativeProceduresRequest
    serializer_class = serializers.AdministrativeProceduresRequestSerializer

    def get(self, request):
        model_object = self.model_class.objects.all()
        serializer_object = self.serializer_class(model_object, many=True)
        data = {
            'message': "Ejecutado con éxito",
            'status': "success",
            'status_code': status.HTTP_200_OK,
            'data': serializer_object.data
        }
        return Response(data)

    def post(self, request):
        serializer_object = self.serializer_class(data=request.data)
        if serializer_object.is_valid():
            serializer_object.save()
            data = {
                'message': "Ejecutado con éxito",
                'status': "success",
                'status_code': status.HTTP_201_CREATED,
                'data': serializer_object.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        else:
            data = {
                'message': "Error al ejecutar",
                'status': "error",
                'status_code': status.HTTP_400_BAD_REQUEST,
                'data': serializer_object.errors
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
