from rest_framework import serializers

from api.models import People, Planet


class PeopleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    homeworld = serializers.PrimaryKeyRelatedField(
        queryset=Planet.objects.all())
    height = serializers.IntegerField()
    mass = serializers.IntegerField()
    hair_color = serializers.ChoiceField(choices=People.HAIR_COLOR_CHOICES)
    created = serializers.DateTimeField()


class PeopleModelSerializer(serializers.ModelSerializer):
    pass
