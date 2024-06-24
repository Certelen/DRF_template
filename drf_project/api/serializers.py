from rest_framework import serializers

from api.models import Ad


class AdSerializer(serializers.ModelSerializer):

    class Meta:
        fields = "__all__"
        model = Ad
