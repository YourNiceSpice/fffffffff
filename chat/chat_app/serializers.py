from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Room,Message



class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
        ]
        extra_kwargs = {"id": {"read_only": True}, "password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        return user


class RoomsListSerializer(serializers.ModelSerializer):
    """Список комнат"""

    class Meta:
        model = Room
        fields = ("room_name",)

class RoomsDetailsSerializer(serializers.ModelSerializer):
    """Содержимое комнаты"""

    class Meta:
        model = Message
        fields = ("message","sender")

class MessageCreateSerializer(serializers.ModelSerializer):
    """Добавление сообщения"""

    class Meta:
        model = Message
        fields = "__all__"

class RoomCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("room_name",)