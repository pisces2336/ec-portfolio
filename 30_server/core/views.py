from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class BaseAPIView(APIView):
    permission_classes = (IsAuthenticated,)
