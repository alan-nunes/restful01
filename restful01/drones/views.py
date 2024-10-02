from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from drones.models import DronesCategory, Drone, Pilot, Competition
from drones.serializers import (
    DroneCategorySerializer,
    DroneSerializer,
    PilotSerializer,
    PilotCompetitonSerializer,
)

from rest_framework import viewsets
from drones.filters import CompetitionFilter
# Create your views here.

class ApiRoot(generics.GenericAPIView):
    name = "api-root"
    
    def get(self, request, *agrs, **kwargs):
        return Response(
            {
                "drone-categories" : reverse("dronecategory-list", request=request),
                "drones": reverse(DroneList.name, request=request),
                "pilots": reverse(PilotList.name, request=request),
                "competitions": reverse(CompetitionList.name, request=request),
            }
        )

class DroneCategoryViewSet(viewsets.ModelViewSet):
    queryset = DronesCategory.objects.all()
    serializer_class = DroneCategorySerializer
     # O 'name' não é necessário aqui porque o router gera os nomes automaticamente
     
    search_fields = ("^name",)
    ordering_fields = ("name")
    
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"
    
    filterset_fields = (
        "drone_category",
        "has_it_completed",
    )
    
    search_fields = ("^name",)
    ordering_fields = (
        "name",
        "manufacturing_date",
    )

class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"
    
class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"
    
    filterset_fields = (
        "gender",
        "races_count",
    )
    
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")  #ordenação

class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"

class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitonSerializer
    name = "competition-list"
    
    filterset_class = CompetitionFilter
    ordering_fields = (
        "distance_in_feet",
        "distance_achievement_date",
    )

class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitonSerializer
    name = "competition-detail"