from rest_framework.response import Response

from .models import Room,Message
from .serializers import RoomsDetailsSerializer
from rest_framework.views import exception_handler
from rest_framework.exceptions import NotAuthenticated,AuthenticationFailed
from rest_framework.response import Response


def custom_exc(exc, context):
    if isinstance(exc, NotAuthenticated):
        return Response("Err:пожалуйста,зарегестрируйтесь и получите токен client --signup", status=401)
    if isinstance(exc,AuthenticationFailed):
        return Response("Err:указан неверный токен client --signup", status=401)

    # else
    # default case
    return exception_handler(exc, context)
def get_message(room_name):
    room_id = Room.objects.get(room_name=room_name).id
    messages = Message.objects.filter(room_name=room_id)
    serializer = RoomsDetailsSerializer(messages, many=True)
    return serializer