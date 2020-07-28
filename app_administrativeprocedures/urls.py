from django.urls import path
from app_administrativeprocedures import views

urlpatterns = [
    path('unidades/', views.Unit.as_view(), name='unidad'),
    path('facultades/', views.UniversityFaculty.as_view(), name='facultad'),
    path('denominaciones/', views.AdministrativeProceduresDenominationGlobal.as_view(), name='denominacion_global'),
    path('procedimientos_administrativos/', views.AdministrativeProcedures.as_view(),
         name='procedimientos_administrativos'),
    path('requisitos_procedimientos_administrativos/', views.AdministrativeProceduresRequest.as_view(),
         name='requisitos_procedimientos_Administrativos'),
    path('ask/', views.AskChatBot.as_view(), name='ask'),
]
