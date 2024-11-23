from uuid import UUID

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Role
from .serializers import RoleSerializer


class RoleCreateListView(APIView):
    # Create
    def post(self, request: Request):
        seliarizer = RoleSerializer(data=request.data)
        seliarizer.is_valid(raise_exception=True)
        seliarizer.save()
        return Response({"role": seliarizer.data})

    # List
    def get(self, request: Request):
        qs = Role.objects.all()
        seliarizer = RoleSerializer(qs, many=True)
        return Response({"roles": seliarizer.data})


class RoleDetailUpdateDeleteView(APIView):
    # Detail
    def get(self, request: Request, id: UUID):
        role = get_or_404(Role, id=id)
        seliarizer = RoleSerializer(role)
        return Response({"role": seliarizer.data})

    # Update
    def patch(self, request: Request, id: UUID):
        role = get_or_404(Role, id=id)
        seliarizer = RoleSerializer(instance=role, data=request.data, partial=True)
        seliarizer.is_valid(raise_exception=True)
        seliarizer.save()
        return Response({"role": seliarizer.data})

    # Delete
    def delete(self, request: Request, id: UUID):
        role = get_or_404(Role, id=id)
        role.delete()
        return Response()

        return Response()
