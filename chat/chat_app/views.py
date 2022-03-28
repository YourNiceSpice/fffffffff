from django.shortcuts import redirect
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Room
from .serializers import RoomsListSerializer, MessageCreateSerializer,RegistrationSerializer,RoomCreateSerializer

from .service import get_message
from rest_framework.permissions import IsAuthenticated


from rest_framework.authtoken.models import Token


class RoomListView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomsListSerializer(rooms, many=True)
        return Response(serializer.data)

class RoomDetailsView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self,request, room_name):

        #add list own_tables



        response = get_message(room_name)
        return Response(response.data)

class MessageCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    """Добавление сообщения"""
    def post(self, request,room_name):

        room_id = Room.objects.get(room_name=room_name).id
        request.data['room_name'] = room_id
        i = Token.objects.get(key=request.data['sender']).user
        request.data['sender'] = i.username


        review = MessageCreateSerializer(data=request.data)
        response = get_message(room_name)

        if review.is_valid():
            review.save()
            return Response(response.data)
        return Response(response.errors, status=status.HTTP_400_BAD_REQUEST)

class RegistrationView(APIView):

    def post(self, request):
        registration_serializer = RegistrationSerializer(data=request.data)

        if registration_serializer.is_valid():
            user = registration_serializer.save()
            token = Token.objects.create(user=user)
            res = registration_serializer.data
            res['token'] = token.pk
            return Response(
                res
            )
        return Response(
            {
                "error": registration_serializer.errors,
                "status": f"{status.HTTP_203_NON_AUTHORITATIVE_INFORMATION} \
        NON AUTHORITATIVE INFORMATION",})



class RoomCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request,):


        room_data = RoomCreateSerializer(data=request.data)
        if room_data.is_valid():
            room_data.save()
            return Response(room_data.data)
        return Response(room_data.errors, status=status.HTTP_400_BAD_REQUEST)



