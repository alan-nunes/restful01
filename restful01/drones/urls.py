from django.urls import path, include
from .import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register("drone-categories", views.DroneCategoryViewSet, basename="dronecategory")

urlpatterns = [
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name), 
    path("", include(router.urls)),
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path("competition/", views.CompetitionList.as_view(), name= views.CompetitionList.name),
    path("competition/<int:pk>/", views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),  
]

#Ao usar SimpleRouter para registrar seu ViewSet, o nome das rotas é gerado automaticamente, e geralmente segue o padrão 
#{basename}-list para a rota de listagem e {basename}-detail para detalhes de um item.
#A adição do basename="dronecategory" garante que as URLs geradas tenham os nomes dronecategory-list e dronecategory-detail.