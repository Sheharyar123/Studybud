from rest_framework import serializers
from base.models import Room


class RoomSerializer(serializers.ModelSerializer):
    topic = serializers.ReadOnlyField(source='topic.name')
    host = serializers.ReadOnlyField(source='host.name')
    participants = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ('id', 'host', 'topic', 'name', 'participants', 'description', 'created_on',)
        