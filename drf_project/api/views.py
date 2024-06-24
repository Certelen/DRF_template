from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from datetime import timedelta
from django.utils import timezone

from api.models import Check, Ad
from api.serializers import AdSerializer
from api.parser import update_ads
from drf_project.settings import CRON


class AdViewSet(viewsets.ModelViewSet):
    serializer_class = AdSerializer
    permission_classes = (IsAuthenticated,)
    ordering = ('-position')

    def get_queryset(self):
        if not CRON:
            zero_point = timezone.now() - timedelta(minutes=1)
            if (not Check.objects.exists() or
                    Check.objects.latest('id').last_check < zero_point):
                update_ads()
        return Ad.objects.all()
