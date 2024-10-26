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

from rest_framework import permissions
from drones import custom_permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from rest_framework.throttling import ScopedRateThrottle
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
    throttle_scope = "drones"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"
    
    filterset_fields = (
        "name",
        "drone_category",
        "manufacturing_date",
        "has_it_completed",
    )
    
    search_fields = ("^name",)
    ordering_fields = (
        "name",
        "manufacturing_date",
    )
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly,
    )
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = "drones"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
        custom_permissions.IsCurrentUserOwnerOrReadOnly
    )
    
class PilotList(generics.ListCreateAPIView):
    throttle_scope = "pilots"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"
    
    filterset_fields = (
        "gender",
        "races_count",
    )
    
    search_fields = ("^name",)
    ordering_fields = ("name", "races_count")  #ordenação
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = "pilots"
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

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