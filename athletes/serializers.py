from rest_framework import serializers

from athletes.models import Athlete
from clubs.models import Club


class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ('id', 'name', 'city', 'country')


class AthleteSerializer(serializers.ModelSerializer):
    club = ClubSerializer(read_only=True)
    club_id = serializers.PrimaryKeyRelatedField(
        queryset=Club.objects.all(),
        source='club',
        write_only=True,
    )

    class Meta:
        model = Athlete
        fields = ('id', 'name', 'gender', 'birth_date', 'belt', 'club', 'club_id')
