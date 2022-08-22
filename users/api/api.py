from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from users.api.serializers import UserSerializer

class UserApiView(APIView):

    def get(self, request):
        users = User.objects.all()
        users_serilizer = UserSerializer(users, many=True)

        return Response(users_serilizer.data)