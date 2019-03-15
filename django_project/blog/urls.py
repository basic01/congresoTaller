from django.urls import path
from . import views


app_name = 'taller'

urlpatterns = [
	path('', views.inicio, name='tallerInicio'),
	path('registro', views.registro, name='tallerRegistro'),
	path('programa', views.programa, name='tallerPrograma'),
	path('talleres', views.talleres, name='tallerTalleres'),
	path('success/<str:tipoExito>', views.exito, name='tallerExito'),
	path('warning/<int:i>-<int:t>/<int:bandera>', views.warning, name='tallerWarning'),
	path('inscripcion/<int:idTaller>', views.inscripcion, name='tallerInscripcion'),

	path('manage', views.administradorInicio, name="administradorInicio"),

	path('manage/general', views.ViewGeneral.as_view(), name="administradorGeneral"),
	path('manage/editarGeneral/<int:idElemento>', views.editarGeneral, name="editarGeneral"),

	path('manage/participantes', views.ViewParticipantes.as_view(), name="administradorParticipantes"),
	path('manage/participantesMondragon', views.participantesMondragon, name="administradorParticipantesMondragon"),
	path('manage/editarParticipante/<int:idElemento>', views.editarParticipante, name="editarParticipante"),
	path('manage/nuevoParticipante', views.nuevoParticipante, name="nuevoParticipante"),
	path('manage/eliminarParticipante/<int:idElemento>', views.eliminarParticipante, name="eliminarParticipante"),

	path('manage/programa', views.ViewPrograma.as_view(), name="administradorPrograma"),
	path('manage/editarPrograma/<int:idElemento>', views.editarPrograma, name="editarPrograma"),
	path('manage/nuevoPrograma', views.nuevoPrograma, name="nuevoPrograma"),
	path('manage/eliminarPrograma/<int:idElemento>', views.eliminarPrograma, name="eliminarPrograma"),

	path('manage/talleres', views.ViewTalleres.as_view(), name="administradorTalleres"),
	path('manage/editarTaller/<int:idElemento>', views.editarTaller, name="editarTaller"),
	path('manage/nuevoTaller', views.nuevoTaller, name="nuevoTaller"),
	path('manage/eliminarTaller/<int:idElemento>', views.eliminarTaller, name="eliminarTaller"),
	
	path('manage/inscripciones', views.ViewInscripciones.as_view(), name="administradorInscripciones"),
	path('manage/editarInscripcion/<int:idElemento>', views.editarInscripcion, name="editarInscripcion"),
	path('manage/nuevoInscripcion', views.nuevoInscripcion, name="nuevoInscripcion"),
	path('manage/eliminarInscripcion/<int:idElemento>', views.eliminarInscripcion, name="eliminarInscripcion"),
]
