from django.db.models import Q
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly

from athletes.models import Athlete
from athletes.serializers import AthleteSerializer


class AthletesListApiView(ListCreateAPIView):
    serializer_class = AthleteSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        qs = Athlete.objects.select_related('club').all()
        QUERY_LOOKUP_PARAMS = {
            "belt": lambda x: Q(belt__iexact=x),
            "gender": lambda x: Q(gender__iexact=x),
            "club_id": lambda x: Q(club_id=x)
        }

        for param in self.request.query_params:
            lookup_func = QUERY_LOOKUP_PARAMS.get(param)
            if lookup_func:
                qs = qs.filter(lookup_func(self.request.query_params[param]))

        return qs


class AthleteDetailApiView(RetrieveUpdateDestroyAPIView):
    queryset = Athlete.objects.select_related('club').all()
    serializer_class = AthleteSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]