from django.urls import path, include
from .import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = SimpleRouter()
#router.register("drone-categories", views.DroneCategoryViewSet)

urlpatterns = [  
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drone-categories/", views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
    path("drone-categories/<int:pk>", views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),
    path("drones/<int:pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<int:pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path("competition/", views.CompetitionList.as_view(), name= views.CompetitionList.name),
    path("competition/<int:pk>/", views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),
    path("", include(router.urls)),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]

#Ao usar SimpleRouter para registrar seu ViewSet, o nome das rotas é gerado automaticamente, e geralmente segue o padrão 
#{basename}-list para a rota de listagem e {basename}-detail para detalhes de um item.
#A adição do basename="dronecategory" garante que as URLs geradas tenham os nomes dronecategory-list e dronecategory-detail.